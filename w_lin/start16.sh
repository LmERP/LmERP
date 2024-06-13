#!/usr/env/bin bash
cd /home/www/w_pro/pro_lxxerp/codes/v1.0_lxxerp16/
source venv_ts/bin/activate
#source venv_sho/bin/activate
#source venv_prd/bin/activate
python3 lxxerp-bin -c lxxerp_ts.conf --dev=all
