class GlobsterHome:
    SQL_URL = r'C:\SIMPLY_Official\2024\TechHome24\drfcore'
    path2directory = r"C:\SIMPLY_Official\2024\TechHome24\drfcore\home\mylibs\data\Mapper\\"
    EquitySctocks_JAN24_752 = ['LICI', 'IOC', 'BPCL', 'JINDALSTEL', 'TATASTEEL', 'TITAN', 'ITC', 'CHOLAFIN', 'PIDILITIND', 'ABB', 'MARUTI', 'SHREECEM', 'LT', 'JSWSTEEL', 'ASIANPAINT', 'GAIL', 'HINDALCO', 'DABUR', 'TATAMOTORS', 'PIIND', 'ONGC', 'SRF', 'COLPAL', 'MARICO', 'TVSMOTOR', 'GRASIM', 'HEROMOTOCO', 'HDFCBANK', 'MCDOWELL-N', 'BANKBARODA', 'ULTRACEMCO', 'APOLLOHOSP', 'ZOMATO', 'BERGEPAINT', 'AXISBANK', 'PNB', 'VEDL', 'TATAMTRDVR', 'HINDUNILVR', 'CANBK', 'KOTAKBANK', 'SBICARD', 'ICICIGI', 'ICICIBANK', 'NESTLEIND', 'HDFCLIFE', 'SBIN', 'MOTHERSON', 'TORNTPHARM', 'DRREDDY', 'TATACONSUM', 'SHRIRAMFIN', 'BAJFINANCE', 'VBL', 'BHARTIARTL', 'BAJAJ-AUTO', 'ICICIPRULI', 'UPL', 'BAJAJHLDNG', 'COALINDIA', 'HAVELLS', 'BAJAJFINSV', 'PGHH', 'ADANIPORTS', 'AMBUJACEM', 'POWERGRID', 'TRENT', 'DMART', 'M&M', 'CIPLA', 'GODREJCP', 'AWL', 'EICHERMOT', 'ADANIENT', 'BRITANNIA', 'MUTHOOTFIN', 'TCS', 'LTIM', 'BEL', 'HAL', 'SUNPHARMA', 'TATAPOWER', 'TECHM', 'INDUSINDBK', 'ATGL', 'BOSCHLTD', 'ZYDUSLIFE', 'SBILIFE', 'RELIANCE', 'INFY', 'IRCTC', 'SIEMENS', 'ADANIGREEN', 'WIPRO', 'NTPC', 'ADANIENSOL', 'HCLTECH', 'DIVISLAB', 'INDIGO', 'DLF', 'NAUKRI', 'IRFC', 'SAIL', 'PAYTM', 'ZEEL', 'POLYCAB', 'YESBANK', 'GUJGASLTD', 'BANKINDIA', 'ESCORTS', 'POLICYBZR', 'PETRONET', 'IDFCFIRSTB', 'BIOCON', 'RVNL', 'NMDC', 'PAGEIND', 'INDIANB', 'MANKIND', 'BHEL', 'UNIONBANK', 'DEVYANI', 'KPITTECH', 'LICHSGFIN', 'RAMCOCEM', 'HINDPETRO', 'MRF', 'FACT', 'FORTIS', 'ALKEM', 'INDUSTOWER', 'IGL', 'ABFRL', 'UBL', 'DIXON', 'AUBANK', 'APOLLOTYRE', 'FLUOROCHEM', 'APLAPOLLO', 'ABCAPITAL', 'DELHIVERY', 'BATAINDIA', 'NHPC', 'COFORGE', 'GODREJPROP', 'M&MFIN', 'BANDHANBNK', 'PEL', 'ASHOKLEY', 'MAXHEALTH', 'RECLTD', 'TORNTPOWER', 'BDL', 'PERSISTENT', 'ASTRAL', 'IPCALAB', 'CGPOWER', 'GLAND', 'JUBLFOOD', 'MAZDOCK', 'MSUMI', 'MPHASIS', 'TATACHEM', 'VOLTAS', 'ACC', 'DEEPAKNTR', 'TATAELXSI', 'MFSL', 'TATACOMM', 'CROMPTON', 'NAVINFLUOR', 'SONACOMS', 'DALBHARAT', 'ADANIPOWER', 'L&TFH', 'LTTS', 'COROMANDEL', 'LAURUSLABS', 'POONAWALLA', 'CUMMINSIND', 'JSWENERGY', 'HDFCAMC', 'INDHOTEL', 'CONCOR', 'SUNTV', 'OIL', 'PFC', 'LUPIN', 'PATANJALI', 'LALPATHLAB', 'FEDERALBNK', 'TIINDIA', 'BHARATFORG', 'SYNGENE', 'OBEROIRLTY', 'AUROPHARMA', 'BALKRISIND', 'PRESTIGE', 'NYKAA', 'LODHA', 'IDEA', 'CGCL', 'ITI', 'PNBHOUSING', 'ASTERDM', 'JMFINANCIL', 'PNCINFRA', 'BORORENEW', 'BSE', 'HINDCOPPER', 'WESTLIFE', 'NIACL', 'MRPL', 'INTELLECT', 'ISEC', 'RBA', 'COCHINSHIP', 'NATIONALUM', 'USHAMART', 'BAYERCROP', 'SKFINDIA', 'SOBHA', 'APARINDS', 'MTARTECH', 'SYRMA', 'AMBER', 'JBMA', 'GESHIP', 'IDBI', 'RALLIS', 'MANAPPURAM', 'DEEPAKFERT', 'JSL', 'AJANTPHARM', 'PCBL', 'IDFC', 'CONCORDBIO', 'GRINFRA', 'NCC', 'CDSL', 'JKPAPER', 'KPIL', 'IRCON', 'GODREJIND', 'KANSAINER', 'CREDITACC', 'RATNAMANI', 'VGUARD', 'WHIRLPOOL', 'TANLA', 'JKCEMENT', 'CENTURYPLY', 'INDIAMART', 'PGHL', 'KEI', 'GMMPFAUDLR', 'SYMPHONY', 'JUBLPHARMA', 'WELCORP', 'EQUITASBNK', 'POLYMED', 'NAZARA', 'TTKPRESTIG', 'GMRINFRA', 'OLECTRA', 'CENTRALBK', 'GLS', 'AEGISCHEM', 'EPIGRAL', 'ELGIEQUIP', 'KPRMILL', 'MCX', 'PRAJIND', 'BIKAJI', 'VINATIORGA', 'UCOBANK', 'KEC', 'MEDANTA', 'HONAUT', 'RADICO', 'ROUTE', 'KIMS', 'STARHEALTH', 'FIVESTAR', 'AIAENG', 'SAPPHIRE', 'RCF', 'KFINTECH', 'GSPL', 'AARTIDRUGS', 'IEX', 'RELAXO', 'BEML', 'LINDEINDIA', 'BALRAMCHIN', 'ZYDUSWELL', 'POWERINDIA', 'MAHLIFE', 'JINDALSAW', 'CHAMBLFERT', 'EIDPARRY', 'TIMKEN', 'VMART', 'CRAFTSMAN', 'JYOTHYLAB', 'GSFC', 'ZFCVINDIA', 'MGL', 'SUMICHEM', 'HEG', 'JBCHEPHARM', 'CERA', 'CLEAN', 'APTUS', 'RAYMOND', '360ONE', 'KAYNES', 'CEATLTD', 'CIEINDIA', 'THERMAX', 'DELTACORP', 'RAIN', 'CHOLAHLDNG', 'CAMPUS', 'EIHOTEL', 'EXIDEIND', 'ENDURANCE', 'SUNDARMFIN', 'BBTC', 'KRBL', 'CAMS', 'EPL', 'NSLNISP', 'RBLBANK', 'BALAMINES', 'IOB', 'TEAMLEASE', 'CCL', 'UNOMINDA', 'UJJIVANSFB', 'TATAINVEST', 'ALLCARGO', 'HINDZINC', 'METROBRAND', 'GRANULES', 'MEDPLUS', 'APLLTD', 'METROPOLIS', 'WELSPUNLIV', 'MASTEK', 'PVRINOX', 'INDIACEM', 'RENUKA', 'JKLAKSHMI', '3MINDIA', 'ALKYLAMINE', 'LUXIND', 'SUPREMEIND', 'JUBLINGREA', 'SUNDRMFAST', 'GICRE', 'KAJARIACER', 'PRINCEPIPE', 'CRISIL', 'GLAXO', 'KNRCON', 'TRIVENI', 'LAXMIMACH', 'IRB', 'SWANENERGY', 'CHEMPLASTS', 'SUPRAJIT', 'SHARDACROP', 'GOCOLORS', 'INGERRAND', 'RAINBOW', 'ASAHIINDIA', 'BLUESTARCO', 'INDIGOPNTS', 'LXCHEM', 'VTL', 'HUDCO', 'CYIENT', 'FINEORG', 'CESC', 'CANFINHOME', 'SUNTECK', 'BRIGADE', 'SONATSOFTW', 'MAHABANK', 'ROSSARI', 'GRINDWELL', 'VIJAYA', 'SHOPERSTOP', 'NLCINDIA', 'GNFC', 'CUB', 'SANOFI', 'BSOFT', 'GPPL', 'GUJALKALI', 'EASEMYTRIP', 'TEJASNET', 'SWSOLAR', 'AETHER', 'AFFLE', 'MAPMYINDIA', 'HOMEFIRST', 'SAFARI', 'KARURVYSYA', 'GODFRYPHLP', 'RAJESHEXPO', 'GRAPHITE', 'RHIM', 'HAPPSTMNDS', 'JAMNAAUTO', 'JUSTDIAL', 'NAM-INDIA', 'ARE&M', 'EMAMILTD', 'ECLERX', 'CENTURYTEX', 'ERIS', 'BIRLACORPN', 'LEMONTREE', 'PFIZER', 'POLYPLEX', 'KSB', 'NUVOCO', 'BCG', 'CSBBANK', 'ACI', 'TRITURBINE', 'ABBOTINDIA', 'ATUL', 'BLS', 'RTNINDIA', 'SFL', 'VARROC', 'PPLPHARMA', 'QUESS', 'FDC', 'ZENSARTECH', 'PHOENIXLTD', 'REDINGTON', 'DATAPATTNS', 'GAEL', 'DCMSHRIRAM', 'SHYAMMETL', 'VIPIND', 'GALAXYSURF', 'INFIBEAM', 'FINPIPE', 'MMTC', 'BLUEDART', 'ANURAS', 'LATENTVIEW', 'MANYAVAR', 'MHRIL', 'AARTIIND', 'RITES', 'SCHAEFFLER', 'NH', 'VAIBHAVGBL', 'STLTECH', 'CARBORUNIV', 'TRIDENT', 'NBCC', 'SJVN', 'NATCOPHARM', 'GLENMARK', 'GILLETTE', 'IIFL', 'SOLARINDS', 'GPIL', 'SAREGAMA', 'TTML', 'CASTROLIND', 'UTIAMC', 'HLEGLAS', 'HFCL', 'CHALET', 'OFSS', 'AAVAS', 'FINCABLES', 'SUVENPHAR', 'MOTILALOFS', 'SPARC', 'MINDACORP', 'FSL', 'KALYANKJIL', 'ENGINERSIN', 'ORIENTELEC', 'TV18BRDCST', 'IBULHSGFIN', 'SUZLON', 'PRSMJOHNSN', 'NETWORK18', 'ALOKINDS', 'AVANTIFEED', 'ANGELONE', 'DBCORP', 'DISHTV', 'HATHWAY', 'MOIL', 'NFL', 'SOUTHBANK', 'MSTCLTD', 'GRAVITA', 'HERITGFOOD', 'SUNFLAG', 'NEWGEN', 'HSCL', 'AHLUCONT', 'ARVINDFASN', 'GET&D', 'J&KBANK', 'BECTORFOOD', 'PDSL', 'SBCL', 'SULA', 'IKIO', 'JWL', 'NAVA', 'KKCL', 'TCI', 'TMB', 'ASTRAZEN', 'CARTRADE', 'MAHSEAMLES', 'KSCL', 'RATEGAIN', 'TATAMETALI', 'ZENTEC', 'SARDAEN', 'HEMIPROP', 'TINPLATE', 'MASFIN', 'ASHOKA', 'WSTCSTPAPR', 'GREENPANEL', 'INDOCO', 'RELIGARE', 'SOMANYCERA', 'IONEXCHANG', 'DOLLAR', 'SUDARSCHEM', 'CAPLIPOINT', 'VOLTAMP', 'LANDMARK', 'OPTIEMUS', 'WELENT', 'SURYAROSNI', 'KOLTEPATIL', 'IFBIND', 'INDIAGLYCO', 'TIPSINDLTD', 'DCXINDIA', 'GOKEX', 'SIYSIL', 'GMDCLTD', 'HNDFDS', 'LLOYDSENGG', 'CHENNPETRO', 'TITAGARH', 'POWERMECH', 'AGI', 'DCAL', 'SHILPAMED', 'UNICHEMLAB', 'NEOGEN', 'PTCIL', 'GARFIBRES', 'JKTYRE', 'VESUVIUS', 'TCIEXP', 'NRBBEARING', 'LTFOODS', 'TARSONS', 'VRLLOG', 'BARBEQUE', 'KIRLOSENG', 'ADVENZYMES', 'RKFORGE', 'GANESHHOUC', 'MOLDTKPAC', 'RUPA', 'ELECTCAST', 'PSPPROJECT', 'DREAMFOLKS', 'AVALON', 'HEIDELBERG', 'JKIL', 'NESCO', 'NEULANDLAB', 'IMFA', 'DALMIASUG', 'UJJIVAN', 'STYLAMIND', 'GHCL', 'ETHOSLTD', 'SHAREINDIA', 'TCNSBRANDS', 'TECHNOE', 'PGEL', 'APCOTEXIND', 'PARADEEP', 'CARERATING', 'MARKSANS', 'TVSSCS', 'ISGEC', 'DWARKESH', 'GLOBUSSPR', 'TATVA', 'AARTIPHARM', 'GREENLAM', 'SBFC', 'LAOPALA', 'UFLEX', 'APOLLOPIPE', 'PARAS', 'WABAG', 'DIVGIITTS', 'PRIVISCL', 'DCBBANK', 'BAJAJHIND', 'COSMOFIRST', 'BAJAJCON', 'EVEREADY', 'CAMLINFINE', 'HGS', 'HCG', 'ESABINDIA', 'GRSE', 'ACLGATI', 'RAMKY', 'SCHNEIDER', 'KIRLPNU', 'HBLPOWER', 'WONDERLA', 'RESPONIND', 'PRUDENT', 'MAITHANALL', 'JINDALPOLY', 'STAR', 'KIRIINDUS', 'ITDCEM', 'ROLEXRINGS', 'SCI', 'SEQUENT', 'HINDWAREAP', 'PTC', 'CIGNITITEC', 'GUFICBIO', 'TIIL', 'MANINFRA', 'HGINFRA', 'SPLPETRO', 'VSTTILLERS', 'SHANTIGEAR', 'STARCEMENT', 'SSWL', 'ASTEC', 'HARSHA', 'TIDEWATER', 'PAISALO', 'GREENPLY', 'NAVNETEDUL', 'GODREJAGRO', 'IOLCP', 'SANSERA', 'DATAMATICS', 'MAYURUNIQ', 'CONFIPET', 'ASTRAMICRO', 'RAILTEL', 'VENKEYS', 'KTKBANK', 'RAJRATAN', 'HINDOILEXP', 'ARVIND', 'AUTOAXLES', 'GABRIEL', 'CMSINFO', 'SIS', 'BEPL', 'EDELWEISS', 'KRSNAA', 'JISLJALEQS', 'FINOPB', 'GREAVESCOT', 'ICIL', 'SUPRIYA', 'HIKAL', 'TDPOWERSYS', 'STYRENIX', 'JCHAC', 'ACE', 'TI', 'RPOWER', 'BOMDYEING', 'MAHLOG', 'DODLA', 'JINDWORLD', 'ORIENTCEM', 'CHOICEIN', 'TIMETECHNO', 'MIDHANI', 'TEGA', 'UNIPARTS', 'MOL', 'DBL', 'CARYSIL', 'EMUDHRA', 'TIRUMALCHM', 'HIL', 'THYROCARE', 'THOMASCOOK', 'RTNPOWER', 'JAICORPLTD', 'AMIORG', 'DEN', 'INOXWIND', 'FIEMIND', 'NOCIL', 'JTEKTINDIA', 'GATEWAY', 'ANANTRAJ', 'FCL', 'ANANDRATHI', 'IFCI', 'SPANDANA', 'FUSION', 'BALMLAWRIE', 'IBREALEST', 'JTLIND', 'KIRLOSBROS', 'DHANI', 'LGBBROSLTD', 'ELECON', 'PRICOLLTD', 'WOCKPHARMA', 'JPASSOCIAT', 'EMIL', 'HCC', 'RELINFRA', 'ACCELYA', 'SAKSOFT', 'JPPOWER', 'DBREALTY', 'SUBEXLTD', 'PSB']
    def get_url(self,value):
        url_dict = {
            "nifty50": "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%2050",
            "nifty": "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%2050",
            "nifty200": "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%20200",
            "auto": "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%20AUTO",
            "banks": "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%20BANK",
            "energy": "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%20ENERGY",
            "finance": "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%20FINANCIAL%20SERVICES",
            "fmcg": "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%20FMCG",
            "it": "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%20IT",
            "media": "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%20MEDIA",
            "metals": "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%20METAL",
            "pharma": "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%20PHARMA",
            "realty": "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%20REALTY"
        }
        return url_dict.get(value, "Invalid value")

    # Test the function
    # print(get_url("auto"))  # Should print 'https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%20AUTO'

        