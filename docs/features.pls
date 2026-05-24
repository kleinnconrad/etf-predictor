DO $$
DECLARE
    -- 1. RECORD VARIABLES: These hold the entire row (all 38 tickers) at specific points in time
    v_today RECORD;
    v_past_1m RECORD;   -- The market state 21 days ago
    v_past_3m RECORD;   -- The market state 63 days ago
    v_past_6m RECORD;   -- The market state 126 days ago
    v_future_6m RECORD; -- The market state 126 days in the future
    
    v_target_class INTEGER;
    v_row_counter INTEGER := 0;
BEGIN
    -- ========================================================================
    -- THE 10-YEAR TIMELINE LOOP
    -- Iterating day-by-day through the imputed master calendar
    -- ========================================================================
    FOR v_today IN (
        SELECT 
            date, spy_price, 
            tnx_price, irx_price, vix_price, dxy_price,               -- Macro
            cl_price, gc_price, hg_price,                             -- Metals & Energy
            zc_price, zw_price, le_price,                             -- Agriculture
            hyg_price, tlt_price, lqd_price,                          -- Credit Risk
            xlf_price, xlk_price, xle_price, xbi_price, eem_price,    -- S&P Sectors A
            gdaxi_price, n225_price,                                  -- Global Indices
            xlu_price, xlp_price, xly_price, xlv_price, vnq_price,    -- S&P Sectors B & Real Estate
            btc_price,                                                -- Crypto
            aapl_price, msft_price, nvda_price, brkb_price, jpm_price,-- US Equities
            sap_price, sie_price, bas_price,                          -- DE Equities
            shel_price, azn_price, rio_price,                         -- UK Equities
            t7203_price, t9984_price, t8035_price                     -- JP Equities
        FROM imputed_yahoo_data 
        ORDER BY date ASC
    ) 
    LOOP
        v_row_counter := v_row_counter + 1;
        
        -- --------------------------------------------------------------------
        -- STEP 1: FETCH THE HISTORICAL & FUTURE SNAPSHOTS
        -- We query the exact row for 1 month, 3 months, and 6 months ago, 
        -- plus 6 months into the future.
        -- --------------------------------------------------------------------
        
        -- 1 Month Ago (21 Trading Days)
        SELECT * INTO v_past_1m FROM imputed_yahoo_data 
        WHERE date < v_today.date ORDER BY date DESC OFFSET 20 LIMIT 1;
        
        -- 3 Months Ago (63 Trading Days)
        SELECT * INTO v_past_3m FROM imputed_yahoo_data 
        WHERE date < v_today.date ORDER BY date DESC OFFSET 62 LIMIT 1;
        
        -- 6 Months Ago (126 Trading Days)
        SELECT * INTO v_past_6m FROM imputed_yahoo_data 
        WHERE date < v_today.date ORDER BY date DESC OFFSET 125 LIMIT 1;

        -- 6 Months into the Future (126 Trading Days)
        SELECT * INTO v_future_6m FROM imputed_yahoo_data 
        WHERE date > v_today.date ORDER BY date ASC OFFSET 125 LIMIT 1;


        -- --------------------------------------------------------------------
        -- STEP 2: VERIFY WE ARE IN THE "ACTIVE TRAINING" PHASE
        -- If v_past_6m is NULL, we are in the Warm-Up Phase (Skip row).
        -- If v_future_6m is NULL, we are in the Blind Spot (Live Predict row).
        -- --------------------------------------------------------------------
        IF v_past_6m IS NOT NULL AND v_future_6m IS NOT NULL THEN
            
            -- CALCULATE THE TARGET VARIABLE (Y)
            DECLARE
                v_future_return NUMERIC := (v_future_6m.spy_price / v_today.spy_price) - 1;
            BEGIN
                IF v_future_return > 0.0175 THEN v_target_class := 1;      -- Up
                ELSIF v_future_return < 0.0075 THEN v_target_class := -1;  -- Down
                ELSE v_target_class := 0;                                  -- Flat
                END IF;
            END;

            -- ----------------------------------------------------------------
            -- STEP 3: ASSEMBLE THE FULL FEATURE MATRIX (X)
            -- We now calculate all 114 momentum variables for this specific day
            -- and write them directly into our final training table.
            -- ----------------------------------------------------------------
            INSERT INTO final_training_matrix (
                date, target_class,
                
                -- TARGET ETF MOMENTUM
                spy_1M_ret, spy_3M_ret, spy_6M_ret,
                
                -- MACRO INDICATORS
                tnx_1M_ret, tnx_3M_ret, tnx_6M_ret,
                irx_1M_ret, irx_3M_ret, irx_6M_ret,
                vix_1M_ret, vix_3M_ret, vix_6M_ret,
                dxy_1M_ret, dxy_3M_ret, dxy_6M_ret,

                -- INDUSTRIAL & PRECIOUS METALS
                cl_1M_ret, cl_3M_ret, cl_6M_ret,
                gc_1M_ret, gc_3M_ret, gc_6M_ret,
                hg_1M_ret, hg_3M_ret, hg_6M_ret,

                -- AGRICULTURAL COMMODITIES
                zc_1M_ret, zc_3M_ret, zc_6M_ret,
                zw_1M_ret, zw_3M_ret, zw_6M_ret,
                le_1M_ret, le_3M_ret, le_6M_ret,

                -- CREDIT RISK & BONDS
                hyg_1M_ret, hyg_3M_ret, hyg_6M_ret,
                tlt_1M_ret, tlt_3M_ret, tlt_6M_ret,
                lqd_1M_ret, lqd_3M_ret, lqd_6M_ret,

                -- BROAD SECTORS & GLOBAL INDICES
                xlf_1M_ret, xlf_3M_ret, xlf_6M_ret,
                xlk_1M_ret, xlk_3M_ret, xlk_6M_ret,
                xle_1M_ret, xle_3M_ret, xle_6M_ret,
                xbi_1M_ret, xbi_3M_ret, xbi_6M_ret,
                eem_1M_ret, eem_3M_ret, eem_6M_ret,
                gdaxi_1M_ret, gdaxi_3M_ret, gdaxi_6M_ret,
                n225_1M_ret, n225_3M_ret, n225_6M_ret,

                -- CYCLICAL VS DEFENSIVE
                xlu_1M_ret, xlu_3M_ret, xlu_6M_ret,
                xlp_1M_ret, xlp_3M_ret, xlp_6M_ret,
                xly_1M_ret, xly_3M_ret, xly_6M_ret,
                xlv_1M_ret, xlv_3M_ret, xlv_6M_ret,

                -- ALTERNATIVES
                vnq_1M_ret, vnq_3M_ret, vnq_6M_ret,
                btc_1M_ret, btc_3M_ret, btc_6M_ret,

                -- SYSTEMIC US EQUITIES
                aapl_1M_ret, aapl_3M_ret, aapl_6M_ret,
                msft_1M_ret, msft_3M_ret, msft_6M_ret,
                nvda_1M_ret, nvda_3M_ret, nvda_6M_ret,
                brkb_1M_ret, brkb_3M_ret, brkb_6M_ret,
                jpm_1M_ret, jpm_3M_ret, jpm_6M_ret,

                -- SYSTEMIC EU EQUITIES
                sap_1M_ret, sap_3M_ret, sap_6M_ret,
                sie_1M_ret, sie_3M_ret, sie_6M_ret,
                bas_1M_ret, bas_3M_ret, bas_6M_ret,

                -- SYSTEMIC UK EQUITIES
                shel_1M_ret, shel_3M_ret, shel_6M_ret,
                azn_1M_ret, azn_3M_ret, azn_6M_ret,
                rio_1M_ret, rio_3M_ret, rio_6M_ret,

                -- SYSTEMIC JP EQUITIES
                t7203_1M_ret, t7203_3M_ret, t7203_6M_ret,
                t9984_1M_ret, t9984_3M_ret, t9984_6M_ret,
                t8035_1M_ret, t8035_3M_ret, t8035_6M_ret
            )
            VALUES (
                v_today.date, v_target_class,
                
                -- The explicit percentage change calculations
                (v_today.spy_price / v_past_1m.spy_price) - 1, (v_today.spy_price / v_past_3m.spy_price) - 1, (v_today.spy_price / v_past_6m.spy_price) - 1,
                
                (v_today.tnx_price / v_past_1m.tnx_price) - 1, (v_today.tnx_price / v_past_3m.tnx_price) - 1, (v_today.tnx_price / v_past_6m.tnx_price) - 1,
                (v_today.irx_price / v_past_1m.irx_price) - 1, (v_today.irx_price / v_past_3m.irx_price) - 1, (v_today.irx_price / v_past_6m.irx_price) - 1,
                (v_today.vix_price / v_past_1m.vix_price) - 1, (v_today.vix_price / v_past_3m.vix_price) - 1, (v_today.vix_price / v_past_6m.vix_price) - 1,
                (v_today.dxy_price / v_past_1m.dxy_price) - 1, (v_today.dxy_price / v_past_3m.dxy_price) - 1, (v_today.dxy_price / v_past_6m.dxy_price) - 1,
                
                (v_today.cl_price / v_past_1m.cl_price) - 1,   (v_today.cl_price / v_past_3m.cl_price) - 1,   (v_today.cl_price / v_past_6m.cl_price) - 1,
                (v_today.gc_price / v_past_1m.gc_price) - 1,   (v_today.gc_price / v_past_3m.gc_price) - 1,   (v_today.gc_price / v_past_6m.gc_price) - 1,
                (v_today.hg_price / v_past_1m.hg_price) - 1,   (v_today.hg_price / v_past_3m.hg_price) - 1,   (v_today.hg_price / v_past_6m.hg_price) - 1,
                
                (v_today.zc_price / v_past_1m.zc_price) - 1,   (v_today.zc_price / v_past_3m.zc_price) - 1,   (v_today.zc_price / v_past_6m.zc_price) - 1,
                (v_today.zw_price / v_past_1m.zw_price) - 1,   (v_today.zw_price / v_past_3m.zw_price) - 1,   (v_today.zw_price / v_past_6m.zw_price) - 1,
                (v_today.le_price / v_past_1m.le_price) - 1,   (v_today.le_price / v_past_3m.le_price) - 1,   (v_today.le_price / v_past_6m.le_price) - 1,
                
                (v_today.hyg_price / v_past_1m.hyg_price) - 1, (v_today.hyg_price / v_past_3m.hyg_price) - 1, (v_today.hyg_price / v_past_6m.hyg_price) - 1,
                (v_today.tlt_price / v_past_1m.tlt_price) - 1, (v_today.tlt_price / v_past_3m.tlt_price) - 1, (v_today.tlt_price / v_past_6m.tlt_price) - 1,
                (v_today.lqd_price / v_past_1m.lqd_price) - 1, (v_today.lqd_price / v_past_3m.lqd_price) - 1, (v_today.lqd_price / v_past_6m.lqd_price) - 1,
                
                (v_today.xlf_price / v_past_1m.xlf_price) - 1, (v_today.xlf_price / v_past_3m.xlf_price) - 1, (v_today.xlf_price / v_past_6m.xlf_price) - 1,
                (v_today.xlk_price / v_past_1m.xlk_price) - 1, (v_today.xlk_price / v_past_3m.xlk_price) - 1, (v_today.xlk_price / v_past_6m.xlk_price) - 1,
                (v_today.xle_price / v_past_1m.xle_price) - 1, (v_today.xle_price / v_past_3m.xle_price) - 1, (v_today.xle_price / v_past_6m.xle_price) - 1,
                (v_today.xbi_price / v_past_1m.xbi_price) - 1, (v_today.xbi_price / v_past_3m.xbi_price) - 1, (v_today.xbi_price / v_past_6m.xbi_price) - 1,
                (v_today.eem_price / v_past_1m.eem_price) - 1, (v_today.eem_price / v_past_3m.eem_price) - 1, (v_today.eem_price / v_past_6m.eem_price) - 1,
                (v_today.gdaxi_price / v_past_1m.gdaxi_price) - 1, (v_today.gdaxi_price / v_past_3m.gdaxi_price) - 1, (v_today.gdaxi_price / v_past_6m.gdaxi_price) - 1,
                (v_today.n225_price / v_past_1m.n225_price) - 1, (v_today.n225_price / v_past_3m.n225_price) - 1, (v_today.n225_price / v_past_6m.n225_price) - 1,
                
                (v_today.xlu_price / v_past_1m.xlu_price) - 1, (v_today.xlu_price / v_past_3m.xlu_price) - 1, (v_today.xlu_price / v_past_6m.xlu_price) - 1,
                (v_today.xlp_price / v_past_1m.xlp_price) - 1, (v_today.xlp_price / v_past_3m.xlp_price) - 1, (v_today.xlp_price / v_past_6m.xlp_price) - 1,
                (v_today.xly_price / v_past_1m.xly_price) - 1, (v_today.xly_price / v_past_3m.xly_price) - 1, (v_today.xly_price / v_past_6m.xly_price) - 1,
                (v_today.xlv_price / v_past_1m.xlv_price) - 1, (v_today.xlv_price / v_past_3m.xlv_price) - 1, (v_today.xlv_price / v_past_6m.xlv_price) - 1,
                
                (v_today.vnq_price / v_past_1m.vnq_price) - 1, (v_today.vnq_price / v_past_3m.vnq_price) - 1, (v_today.vnq_price / v_past_6m.vnq_price) - 1,
                (v_today.btc_price / v_past_1m.btc_price) - 1, (v_today.btc_price / v_past_3m.btc_price) - 1, (v_today.btc_price / v_past_6m.btc_price) - 1,
                
                (v_today.aapl_price / v_past_1m.aapl_price) - 1, (v_today.aapl_price / v_past_3m.aapl_price) - 1, (v_today.aapl_price / v_past_6m.aapl_price) - 1,
                (v_today.msft_price / v_past_1m.msft_price) - 1, (v_today.msft_price / v_past_3m.msft_price) - 1, (v_today.msft_price / v_past_6m.msft_price) - 1,
                (v_today.nvda_price / v_past_1m.nvda_price) - 1, (v_today.nvda_price / v_past_3m.nvda_price) - 1, (v_today.nvda_price / v_past_6m.nvda_price) - 1,
                (v_today.brkb_price / v_past_1m.brkb_price) - 1, (v_today.brkb_price / v_past_3m.brkb_price) - 1, (v_today.brkb_price / v_past_6m.brkb_price) - 1,
                (v_today.jpm_price / v_past_1m.jpm_price) - 1,  (v_today.jpm_price / v_past_3m.jpm_price) - 1,  (v_today.jpm_price / v_past_6m.jpm_price) - 1,
                
                (v_today.sap_price / v_past_1m.sap_price) - 1, (v_today.sap_price / v_past_3m.sap_price) - 1, (v_today.sap_price / v_past_6m.sap_price) - 1,
                (v_today.sie_price / v_past_1m.sie_price) - 1, (v_today.sie_price / v_past_3m.sie_price) - 1, (v_today.sie_price / v_past_6m.sie_price) - 1,
                (v_today.bas_price / v_past_1m.bas_price) - 1, (v_today.bas_price / v_past_3m.bas_price) - 1, (v_today.bas_price / v_past_6m.bas_price) - 1,
                
                (v_today.shel_price / v_past_1m.shel_price) - 1, (v_today.shel_price / v_past_3m.shel_price) - 1, (v_today.shel_price / v_past_6m.shel_price) - 1,
                (v_today.azn_price / v_past_1m.azn_price) - 1,  (v_today.azn_price / v_past_3m.azn_price) - 1,  (v_today.azn_price / v_past_6m.azn_price) - 1,
                (v_today.rio_price / v_past_1m.rio_price) - 1,  (v_today.rio_price / v_past_3m.rio_price) - 1,  (v_today.rio_price / v_past_6m.rio_price) - 1,
                
                (v_today.t7203_price / v_past_1m.t7203_price) - 1, (v_today.t7203_price / v_past_3m.t7203_price) - 1, (v_today.t7203_price / v_past_6m.t7203_price) - 1,
                (v_today.t9984_price / v_past_1m.t9984_price) - 1, (v_today.t9984_price / v_past_3m.t9984_price) - 1, (v_today.t9984_price / v_past_6m.t9984_price) - 1,
                (v_today.t8035_price / v_past_1m.t8035_price) - 1, (v_today.t8035_price / v_past_3m.t8035_price) - 1, (v_today.t8035_price / v_past_6m.t8035_price) - 1
            );
            
        -- (The logic for the 'Live Prediction' point where v_future_6m IS NULL 
        -- would follow the exact same INSERT pattern, simply omitting the target_class)
        END IF;

    END LOOP;
    
    RAISE NOTICE 'Processed % rows. Feature Engineering Complete.', v_row_counter;
END; $$;