import streamlit as st
import pandas as pd
import numpy as np
import chart_studio.plotly as plotly
import plotly.figure_factory as ff
from plotly import graph_objs as go
from prophet import Prophet
from prophet.plot import plot_plotly




st.title('Stock Trend Analyzer App')

dataset = ('20MICRONS_data',	'3IINFOTECH_data',	'3MINDIA_data',	'A2ZMES_data',	'AANJANEYA_data',	'AARTIDRUGS_data',	'AARTIIND_data',	'AARVEEDEN_data',	'ABAN_data',	'ABB_data',	'ABCIL_data',	'ABGSHIP_data',	'ABIRLANUVO_data',	'ACC_data',	'ACE_data',	'ACKRUTI_data',	'ADANIENT_data',	'ACROPETAL_data',	'ADANIPOWER_data',	'ADFFOODS_data',	'ADHUNIK_data',	'ADORWELD_data',	'ADSL_data',	'ADVANIHOTR_data',	'ADVANTA_data',	'AEGISCHEM_data',	'AFL_data',	'AFTEK_data',	'AGCNET_data',	'AGRODUTCH_data',	'AHLEAST_data',	'AHLUCONT_data',	'AHLWEST_data',	'AHMEDFORGE_data',	'AIAENG_data',	'AICHAMP_data',	'AJANTPHARM_data',	'AJMERA_data',	'AKSHOPTFBR_data',	'AKZOINDIA_data',	'ALBK_data',	'ALCHEM_data',	'ALEMBICLTD_data',	'ALFALAVAL_data',	'ALICON_data',	'ALKALI_data',	'ALKYLAMINE_data',	'ALLCARGO_data',	'ALLSEC_data',	'ALMONDZ_data',	'ALOKTEXT_data',	'ALPHAGEO_data',	'AMAR_data',	'AMARAJABAT_data',	'ALPSINDUS_data',	'AMBIKCO_data',	'AMBUJACEM_data',	'AMDIND_data',	'AMTEKAUTO_data',	'AMTEKINDIA_data',	'ANANTRAJ_data',	'ANDHRABANK_data',	'ANDHRSUGAR_data',	'ANGIND_data',	'ANIKINDS_data',	'ANDHRACEMT_data',	'ANKURDRUGS_data',	'ANSALAPI_data',	'ANSALHSG_data',	'ANTGRAPHIC_data',	'APARINDS_data',	'APCOTEXIND_data',	'APIL_data',	'APOLLOHOSP_data',	'APOLLOTYRE_data',	'APPAPER_data',	'APTECHT_data',	'AQUA_data',	'ARCHIDPLY_data',	'ARCHIES_data',	'AREVAT&D_data',	'ARIES_data',	'ARIHANT_data',	'ARL_data',	'AROGRANITE_data',	'ARROWTEX_data',	'ARSHIYA_data',	'ARSSINFRA_data',	'ARVIND_data',	'ASAHIINDIA_data',	'ASAL_data',	'ASHAPURMIN_data',	'ASHCONIUL_data',	'ASHIANA_data',	'ASHIMASYN_data',	'ASHOKA_data',	'ASHOKLEY_data',	'ASIANELEC_data',	'ASIANHOTNR_data',	'ASIANPAINT_data',	'ASIANTILES_data',	'ASIL_data',	'ASSAMCO_data',	'ASTEC_data',	'ASTERSILI_data',	'ASTRAL_data',	'ASTRAMICRO_data',	'ASTRAZEN_data',	'ATFL_data',	'ATLANTA_data',	'ATLASCYCLE_data',	'ATNINTER_data',	'ATUL_data',	'AURIONPRO_data',	'AUROPHARMA_data',	'AUSOMENT_data',	'AUSTRAL_data',	'AUTOAXLES_data',	'AUTOIND_data',	'AUTOLITIND_data',	'AVANTI_data',	'AVENTIS_data',	'AVTNPL_data',	'AXISBANK_data',	'AXIS-IT&T_data',	'BAGFILMS_data',	'BAJAJ-AUTO_data',	'BAJAJCORP_data',	'BAJAJELEC_data',	'BAJAJFINSV_data',	'BAJAJHIND_data',	'BAJAJHLDNG_data',	'BAJFINANCE_data',	'BALAJITELE_data',	'BALAMINES_data',	'BALKRISIND_data',	'BALLARPUR_data',	'BALMLAWRIE_data',	'BALPHARMA_data',	'BALRAMCHIN_data',	'BANARISUG_data',	'BANCOINDIA_data',	'BANG_data',	'BANKBARODA_data',	'BANKINDIA_data',	'BANSWRAS_data',	'BARTRONICS_data',	'BASF_data',	'BASML_data',	'BATAINDIA_data',	'BATLIBOI_data',	'BBL_data',	'BBTC_data',	'BEDMUTHA_data',	'BEL_data',	'BELLCERATL_data',	'BEML_data',	'BEPL_data',	'BERGEPAINT_data',	'BFINVEST_data',	'BFUTILITIE_data',	'BGRENERGY_data',	'BHAGWATIHO_data',	'BHAGYNAGAR_data',	'BHARATFORG_data',	'BHARATGEAR_data',	'BHARATRAS_data',	'BHARTIARTL_data',	'BHARTISHIP_data',	'BHEL_data',	'BHUSANSTL_data',	'BIL_data',	'BILPOWER_data',	'BINANIIND_data',	'BINDALAGRO_data',	'BIOCON_data',	'BIRLACORPN_data',	'BIRLACOT_data',	'BIRLAERIC_data',	'BIRLAMONEY_data',	'BIRLAPOWER_data',	'BLBLIMITED_data',	'BLISSGVS_data',	'BLKASHYAP_data',	'BLUECHIP_data',	'BLUECOAST_data',	'BLUEDART_data',	'BLUESTARCO_data',	'BLUESTINFO_data',	'BOC_data',	'BOMDYEING_data',	'BOSCHLTD_data',	'BPCL_data',	'BPL_data',	'BRANDHOUSE_data',	'BRFL_data',	'BRIGADE_data',	'BRITANNIA_data',	'BROADCAST_data',	'BSELINFRA_data',	'BSL_data',	'BSTRANSCOM_data',	'BURNPUR_data',	'BVCL_data',	'CADILAHC_data',	'CAIRN_data',	'CALSOFT_data',	'CAMBRIDGE_data',	'CAMLIN_data',	'CANBK_data',	'CANDC_data',	'CANFINHOME_data',	'CANTABIL_data',	'CARBORUNIV_data',	'CAROLINFO_data',	'CASTROL_data',	'CCCL_data',	'CCL_data',	'CEATLTD_data',	'CEBBCO_data',	'CELESTIAL_data',	'CENTENKA_data',	'CENTEXT_data',	'CENTRALBK_data',	'CENTUM_data',	'CENTURYPLY_data',	'CENTURYTEX_data',	'CERA_data',	'CESC_data',	'CHAMBLFERT_data',	'CHEMFALKAL_data',	'CHEMPLAST_data',	'CHENNPETRO_data',	'CHESLINTEX_data',	'CHETTINAD_data',	'CHOLAFIN_data',	'CILNOVA_data',	'CINEMAX_data',	'CINEVISTA_data',	'CIPLA_data',	'CLASSIC_data',	'CLNINDIA_data',	'CLUTCHAUTO_data',	'CMAHENDRA_data',	'CMC_data',	'COALINDIA_data',	'COLPAL_data',	'CONCOR_data',	'CONSOFINVT_data',	'CORAL-HUB_data',	'CORDSCABLE_data',	'COREPROTEC_data',	'COROMANDEL_data',	'CORPBANK_data',	'COSMOFILMS_data',	'COX&KINGS_data',	'CPIL_data',	'CREATIVEYE_data',	'CRESTANI_data',	'CREWBOS_data',	'CRISIL_data',	'CROMPGREAV_data',	'CRONIMET_data',	'CTE_data',	'CUB_data',	'CUBEXTUB_data',	'CUMMINSIND_data',	'CURATECH_data',	'CYBERMEDIA_data',	'CYBERTECH_data',	'DAAWAT_data',	'DABUR_data',	'DALMIASUG_data',	'DATAMATICS_data',	'DBCORP_data',	'DBREALTY_data',	'DCB_data',	'DCHL_data',	'DCM_data',	'DCMSRMCONS_data',	'DCW_data',	'DECCANCE_data',	'DECOLIGHT_data',	'DEEPAKFERT_data',	'DEEPAKNTR_data',	'DEEPIND_data',	'DELTACORP_data',	'DELTAMAGNT_data',	'DEN_data',	'DENABANK_data',	'DENORA_data',	'DEWANHOUS_data',	'DHAMPURSUG_data',	'DHANBANK_data',	'DHANUKA_data',	'DHANUS_data',	'DHARSUGAR_data',	'DHUNINV_data',	'DIAPOWER_data',	'DICIND_data',	'DIGJAM_data',	'DISHMAN_data',	'DISHTV_data',	'DIVISLAB_data',	'DLF_data',	'DLINKINDIA_data',	'DOLPHINOFF_data',	'DONEAR_data',	'DPSCLTD_data',	'DPTL_data',	'DQE_data',	'DREDGECORP_data',	'DRREDDY_data',	'DSKULKARNI_data',	'DUNCANSIND_data',	'DWARKESH_data',	'DYNAMATECH_data',	'DYNASYS_data',	'EASTSILK_data',	'EASUNREYRL_data',	'ECEIND_data',	'ECLERX_data',	'EDELWEISS_data',	'EDL_data',	'EDSERV_data',	'EDUCOMP_data',	'EICHERMOT_data',	'EIDPARRY_data',	'EIHAHOTELS_data',	'EIHOTEL_data',	'EIMCOELECO_data',	'EKC_data',	'ELDERPHARM_data',	'ELECON_data',	'ELECTCAST_data',	'ELECTHERM_data',	'ELGIEQUIP_data',	'EMAMIINFRA_data',	'EMAMILTD_data',	'EMCO_data',	'EMKAY_data',	'EMMBI_data',	'ENERGYDEV_data',	'ENGINERSIN_data',	'ENIL_data',	'ENTEGRA_data',	'ERAINFRA_data',	'EROSMEDIA_data',	'ESABINDIA_data',	'ESCORTS_data',	'ESL_data',	'ESSAROIL_data',	'ESSARPORTS_data',	'ESSDEE_data',	'ESSELPACK_data',	'ESTER_data',	'EUROCERA_data',	'EUROMULTI_data',	'EUROTEXIND_data',	'EVEREADY_data',	'EVERESTIND_data',	'EVERONN_data',	'EVINIX_data',	'EXCELCROP_data',	'EXCELINDUS_data',	'EXCELINFO_data',	'EXIDEIND_data',	'FACT_data',	'FAGBEARING_data',	'FAME_data',	'FARMAXIND_data',	'FCH_data',	'FCSSOFT_data',	'FDC_data',	'FEDDERLOYD_data',	'FEDERALBNK_data',	'FIEMIND_data',	'FINANTECH_data',	'FINCABLES_data',	'FINPIPE_data',	'FIRSTLEASE_data',	'FIRSTWIN_data',	'FKONCO_data',	'FMGOETZE_data',	'FORTIS_data',	'FOSECOIND_data',	'FOURSOFT_data',	'FSL_data',	'FUTUREVENT_data',	'GABRIEL_data',	'GAEL_data',	'GAIL_data',	'GAL_data',	'GALLANTT_data',	'GALLISPAT_data',	'GAMMNINFRA_data',	'GAMMONIND_data',	'GANDHITUBE_data',	'GANESHHOUC_data',	'GARDENSILK_data',	'GARWALLROP_data',	'GLOBOFFS_data',	'GATI_data',	'GDL_data',	'GEECEE_data',	'GEINDSYS_data',	'GEMINI_data',	'GENESYS_data',	'GENUSPOWER_data',	'GEODESIC_data',	'GEOJITBNPP_data',	'GEOMETRIC_data',	'GESHIP_data',	'GHCL_data',	'GICHSGFIN_data',	'GILLANDERS_data',	'GILLETTE_data',	'GINNIFILA_data',	'GIPCL_data',	'GISOLUTION_data',	'GITANJALI_data',	'GKWLIMITED_data',	'GLAXO_data',	'GLENMARK_data',	'GLFL_data',	'GLOBALVECT_data',	'GLOBUSSPR_data',	'GLODYNE_data',	'GLORY_data',	'GMBREW_data',	'GMDCLTD_data',	'GMRINFRA_data',	'GNFC_data',	'GOACARBON_data',	'GODFRYPHLP_data',	'GODREJCP_data',	'GODREJIND_data',	'GODREJPROP_data',	'GOENKA_data',	'GOKEX_data',	'GOKUL_data',	'GOLDENTOBC_data',	'GOLDIAM_data',	'GOLDINFRA_data',	'GOLDTECH_data',	'GPIL_data',	'GPPL_data',	'GRABALALK_data',	'GRANULES_data',	'GRAPHITE_data',	'GRASIM_data',	'GREAVESCOT_data',	'GREENPLY_data',	'GREENPOWER_data',	'GRINDWELL_data',	'GRUH_data',	'GSFC_data',	'GSKCONS_data',	'GSLNOVA_data',	'GSPL_data',	'GSSAMERICA_data',	'GTL_data',	'GTLINFRA_data',	'GTNIND_data',	'GTOFFSHORE_data',	'GUFICBIO_data',	'GUJALKALI_data',	'GUJAPOLLO_data',	'GUJFLUORO_data',	'GUJNRECOKE_data',	'GUJRATGAS_data',	'GUJSIDHCEM_data',	'GUJSTATFIN_data',	'GULFOILCOR_data',	'GVKPIL_data',	'HALONIX_data',	'HANUNG_data',	'HARITASEAT_data',	'HARRMALAYA_data',	'HATHWAY_data',	'HAVELLS_data',	'HBLPOWER_data',	'HBSTOCK_data',	'HCC_data',	'HCIL_data',	'HCL-INSYS_data',	'HCLTECH_data',	'HDFC_data',	'HDFCBANK_data',	'HDIL_data',	'HEG_data',	'HEIDELBERG_data',	'HELIOSMATH_data',	'HERCULES_data',	'HERITGFOOD_data',	'HEROHONDA_data',	'HEXAWARE_data',	'HFCL_data',	'HGSL_data',	'HIKAL_data',	'HILTON_data',	'HIMATSEIDE_data',	'HINDALCO_data',	'HINDCOMPOS_data',	'HINDCOPPER_data',	'HINDDORROL_data',	'HINDMOTORS_data',	'HINDNATGLS_data',	'HINDOILEXP_data',	'HINDPETRO_data',	'HINDSYNTEX_data',	'HINDUJAFO_data',	'HINDUJAVEN_data',	'HINDUNILVR_data',	'HINDZINC_data',	'HIRECT_data',	'HITACHIHOM_data',	'HITECHGEAR_data',	'HITECHPLAS_data',	'HMT_data',	'HMVL_data',	'HOCL_data',	'HONAUT_data',	'HONDAPOWER_data',	'HOPFL_data',	'HORIZONINF_data',	'HOTELEELA_data',	'HOTELRUGBY_data',	'HOVS_data',	'HSIL_data',	'HTMEDIA_data',	'HYDRBADIND_data',	'IBN18_data',	'IBPOW_data',	'IBREALEST_data',	'IBSEC_data',	'ICICIBANK_data',	'ICIL_data',	'ICRA_data',	'ICSA_data',	'IDBI_data',	'IDEA_data',	'IDFC_data',	'IFBAGRO_data',	'IFBIND_data',	'IFCI_data',	'IFGLREFRAC_data',	'IGARASHI_data',	'IGL_data',	'IGPL_data',	'IITL_data',	'IL&FSENGG_data',	'IL&FSTRANS_data',	'IMFA_data',	'IMPAL_data',	'IMPEXFERRO_data',	'INDBANK_data',	'INDHOTEL_data',	'INDIABULLS_data',	'INDIACEM_data',	'INDIAGLYCO_data',	'INDIAINFO_data',	'INDIANB_data',	'INDIANCARD_data',	'INDIANHUME_data',	'INDLMETER_data',	'INDNIPPON_data',	'INDOASIFU_data',	'INDOCO_data',	'INDORAMA_data',	'INDOSOLAR_data',	'INDOTECH_data',	'INDOWIND_data',	'INDRAMEDCO_data',	'INDSWFTLAB_data',	'INDSWFTLTD_data',	'INDUSFILA_data',	'INDUSINDBK_data',	'INEABS_data',	'INFINITE_data',	'INFOMEDIA_data',	'INFY_data',	'INFOTECENT_data',	'INGERRAND_data',	'INGVYSYABK_data',	'INNOIND_data',	'INOXLEISUR_data',	'INSECTICID_data',	'IOB_data',	'IOC_data',	'IOLCP_data',	'IOLN_data',	'IPCALAB_data',	'IRB_data',	'ISFT_data',	'ISMTLTD_data',	'ISPATIND_data',	'ITC_data',	'ITDCEM_data',	'ITI_data',	'IVC_data',	'IVP_data',	'IVRCLAH_data',	'IVRCLINFRA_data',	'J&KBANK_data',	'JAGRAN_data',	'JAGSNPHARM_data',	'JAIBALAJI_data',	'JAICORPLTD_data',	'JAINSTUDIO_data',	'JAMNAAUTO_data',	'JAYAGROGN_data',	'JAYBARMARU_data',	'JAYNECOIND_data',	'JAYSREETEA_data',	'JBCHEPHARM_data',	'JBFIND_data',	'JBMA_data',	'JCTEL_data',	'JENSONICOL_data',	'JETAIRWAYS_data',	'JEYPORE_data',	'JHS_data',	'JIKIND_data',	'JINDALPHOT_data',	'JINDALPOLY_data',	'JINDALSAW_data',	'JINDALSTEL_data',	'JINDALSWHL_data',	'JINDCOT_data',	'JINDRILL_data',	'JINDWORLD_data',	'JISLJALEQS_data',	'JKCEMENT_data',	'JKIL_data',	'JKLAKSHMI_data',	'JKPAPER_data',	'JKTYRE_data',	'JMCPROJECT_data',	'JMFINANCIL_data',	'JMTAUTOLTD_data',	'JOCIL_data',	'JPASSOCIAT_data',	'JPINFRATEC_data',	'JPPOWER_data',	'JSL_data',	'JSWENERGY_data',	'JSWSTEEL_data',	'JUBILANT_data',	'JUBLFOOD_data',	'JUBLINDS_data',	'JVLAGRO_data',	'JYOTHYLAB_data',	'JYOTISTRUC_data',	'KABRAEXTRU_data',	'KAJARIACER_data',	'KAKATCEM_data',	'KALECONSUL_data',	'KALINDEE_data',	'KALPATPOWR_data',	'KALYANIFRG_data',	'KAMATHOTEL_data',	'KANDAGIRI_data',	'KANORICHEM_data',	'KANSAINER_data',	'KARURVYSYA_data',	'KAUSHALYA_data',	'KAVVERITEL_data',	'KBIL_data',	'KCP_data',	'KCPSUGIND_data',	'KEC_data',	'KECL_data',	'KEI_data',	'KEMROCK_data',	'KERNEX_data',	'KESARENT_data',	'KESORAMIND_data',	'KEYCORPSER_data',	'KFA_data',	'KGL_data',	'KHAITANELE_data',	'KHAITANLTD_data',	'KHANDSE_data',	'KICL_data',	'KIL_data',	'KILITCH_data',	'KINETICMOT_data',	'KIRIINDUS_data',	'KIRLOSBROS_data',	'KIRLOSENG_data',	'KIRLOSIND_data',	'KITPLYIND_data',	'KKCL_data',	'KLGSYSTEL_data',	'KMSUGAR_data',	'KNRCON_data',	'KOHINOOR_data',	'KOLTEPATIL_data',	'KOPDRUGS_data',	'KOPRAN_data',	'KOTAKBANK_data',	'KOTARISUG_data',	'KOTHARIPET_data',	'KOTHARIPRO_data',	'KOUTONS_data',	'KPIT_data',	'KPRMILL_data',	'KRBL_data',	'KRISHNAENG_data',	'KSBPUMPS_data',	'KSCL_data',	'KSERASERA_data',	'KSK_data',	'KSL_data',	'KSOILS_data',	'KTIL_data',	'KTKBANK_data',	'LAKPRE_data',	'LAKSHMIEFL_data',	'LAKSHVILAS_data',	'LANCOIN_data',	'LAOPALA_data',	'LAXMIMACH_data',	'LGBBROSLTD_data',	'LGBFORGE_data',	'LIBERTSHOE_data',	'LICHSGFIN_data',	'LITL_data',	'LLOYDELENG_data',	'LLOYDFIN_data',	'LLOYDSTEEL_data',	'LML_data',	'LOGIXMICRO_data',	'LOKESHMACH_data',	'LOTUSEYE_data',	'LOVABLE_data',	'LPDC_data',	'LT_data',	'LUMAXAUTO_data',	'LUMAXIND_data',	'LUMAXTECH_data',	'LUPIN_data',	'LYKALABS_data',	'M&M_data',	'M&MFIN_data',	'MAANALU_data',	'MADHAV_data',	'MADHUCON_data',	'MADRASCEM_data',	'MADRASFERT_data',	'MAGMA_data',	'MAGNUM_data',	'MAHABANK_data',	'MAHINDFORG_data',	'MAHINDUGIN_data',	'MAHLIFE_data',	'MAHSCOOTER_data',	'MAHSEAMLES_data',	'MALWACOTT_data',	'MANAKSIA_data',	'MANALIPETC_data',	'MANDHANA_data',	'MANGALAM_data',	'MANGCHEFER_data',	'MANGLMCEM_data',	'MANGTIMBER_data',	'MANINDS_data',	'MANINFRA_data',	'MANUGRAPH_data',	'MARALOVER_data',	'MARICO_data',	'MARKSANS_data',	'MARUTI_data',	'MASTEK_data',	'MAWANASUG_data',	'MAX_data',	'MAXWELL_data',	'MBECL_data',	'MBLINFRA_data',	'MCDHOLDING_data',	'MCDOWELL-N_data',	'MCLEODRUSS_data',	'MEGASOFT_data',	'MEGH_data',	'MELSTAR_data',	'MERCK_data',	'MHRIL_data',	'MIC_data',	'MICROSEC_data',	'MICROTECH_data',	'MINDAIND_data',	'MINDTREE_data',	'MIRCELECTR_data',	'MIRZAINT_data',	'MLL_data',	'MMFL_data',	'MMFSL_data',	'MOIL_data',	'MONNETISPA_data',	'MONSANTO_data',	'MORARJETEX_data',	'MOREPENLAB_data',	'MOSERBAER_data',	'MOTHERSUMI_data',	'MOTILALOFS_data',	'MOTOGENFIN_data',	'MPHASIS_data',	'MPSLTD_data',	'MRF_data',	'MRO-TEK_data',	'MRPL_data',	'MSPL_data',	'MTNL_data',	'MUDRA_data',	'MUKANDENGG_data',	'MUKANDLTD_data',	'MUKTAARTS_data',	'MUNDRAPORT_data',	'MUNJALAU_data',	'MUNJALSHOW_data',	'MURLIIND_data',	'MURUDCERA_data',	'MVL_data',	'MVLIND_data',	'MYSOREBANK_data',	'NAGARFERT_data',	'NAGREEKCAP_data',	'NAGREEKEXP_data',	'NAHARCAP_data',	'NAHARINDUS_data',	'NAHARPOLY_data',	'NAHARSPING_data',	'NANDAN_data',	'NATCOPHARM_data',	'NATIONALUM_data',	'NATNLSTEEL_data',	'NAUKRI_data',	'NAVINFLUOR_data',	'NAVNETPUBL_data',	'NBVENTURES_data',	'NCC_data',	'NCLIND_data',	'NDTV_data',	'NECLIFE_data',	'NELCAST_data',	'NELCO_data',	'NEPCMICON_data',	'NESCO_data',	'NET4_data',	'NETWORK18_data',	'NEULANDLAB_data',	'NEXTMEDIA_data',	'NEYVELILIG_data',	'NFL_data',	'NHPC_data',	'NICCO_data',	'NIITLTD_data',	'NIITTECH_data',	'NILKAMAL_data',	'NIPPOBATRY_data',	'NIRMA_data',	'NISSAN_data',	'NITCO_data',	'NITESHEST_data',	'NITINFIRE_data',	'NITINSPIN_data',	'NMDC_data',	'NOCIL_data',	'NOIDATOLL_data',	'NORBTEAEXP_data',	'NORTHGATE_data',	'NOVOPANIND_data',	'NRBBEARING_data',	'NSIL_data',	'NTPC_data',	'NUCENT_data',	'NUCHEM_data',	'NUCLEUS_data',	'NUMERICPW_data',	'NUTEK_data',	'OBEROIRLTY_data',	'OCL_data',	'OFSS_data',	'OIL_data',	'OILCOUNTUB_data',	'OISL_data',	'OMAXAUTO_data',	'OMAXE_data',	'OMKARCHEM_data',	'OMMETALS_data',	'OMNITECH_data',	'ONGC_data',	'ONMOBILE_data',	'ONWARDTEC_data',	'OPTOCIRCUI_data',	'ORBITCORP_data',	'ORCHIDCHEM_data',	'ORIENTABRA_data',	'ORIENTALTL_data',	'ORIENTBANK_data',	'ORIENTCERA_data',	'ORIENTHOT_data',	'ORIENTLTD_data',	'ORIENTPPR_data',	'ORISSAMINE_data',	'OUDHSUG_data',	'PAEL_data',	'PAGEIND_data',	'PANACEABIO_data',	'PANORAMUNI_data',	'PANTALOONR_data',	'PAPERPROD_data',	'PARABDRUGS_data',	'PARACABLES_data',	'PARAL_data',	'PARAPRINT_data',	'PARASPETRO_data',	'PAREKHPLAT_data',	'PARRYSUGAR_data',	'PARSVNATH_data',	'PATELENG_data',	'PATINTLOG_data',	'PATNI_data',	'PATSPINLTD_data',	'PBAINFRA_data',	'PDPL_data',	'PDUMJEIND_data',	'PDUMJEPULP_data',	'PEARLPOLY_data',	'PENIND_data',	'PENINLAND_data',	'PEPL_data',	'PERSISTENT_data',	'PETRONENGG_data',	'PETRONET_data',	'PFC_data',	'PFIZER_data',	'PFOCUS_data',	'PFS_data',	'PGHH_data',	'PHILIPCARB_data',	'PHOENIXLTD_data',	'PIDILITIND_data',	'PIIND_data',	'PIONDIST_data',	'PIPAVAVYD_data',	'PIRGLASS_data',	'PIRHEALTH_data',	'PIRLIFE_data',	'PITTILAM_data',	'PLASTIBLEN_data',	'PLETHICO_data',	'PNB_data',	'PNBGILTS_data',	'PNC_data',	'POCHIRAJU_data',	'POLARIS_data',	'POLYPLEX_data',	'PONNIERODE_data',	'POWERGRID_data',	'PPAP_data',	'PRADIP_data',	'PRAENG_data',	'PRAJIND_data',	'PRAKASH_data',	'PRAKASHSTL_data',	'PRATIBHA_data',	'PRECOT_data',	'PRECWIRE_data',	'PREMIER_data',	'PRESTIGE_data',	'PRICOL_data',	'PRIMESECU_data',	'PRISMCEM_data',	'PRITHVI_data',	'PROVOGUE_data',	'PSB_data',	'PSL_data',	'PTC_data',	'PTL_data',	'PUNJABCHEM_data',	'PUNJLLOYD_data',	'PURVA_data',	'PVP_data',	'PVR_data',	'QUINTEGRA_data',	'RADAAN_data',	'RADICO_data',	'RAINBOWPAP_data',	'RAINCOM_data',	'RAIREKMOH_data',	'RAJESHEXPO_data',	'RAJOIL_data',	'RAJRAYON_data',	'RAJSREESUG_data',	'RAJTV_data',	'RAJVIR_data',	'RALLIS_data',	'RAMANEWS_data',	'RAMCOIND_data',	'RAMCOSYS_data',	'RAMKY_data',	'RAMSARUP_data',	'RANASUG_data',	'RANBAXY_data',	'RANEENGINE_data',	'RANEHOLDIN_data',	'RATNAMANI_data',	'RAYMOND_data',	'RBL_data',	'RBN_data',	'RCF_data',	'RCOM_data',	'RECLTD_data',	'REDINGTON_data',	'REFEX_data',	'REIAGROLTD_data',	'REISIXTEN_data',	'RELAXO_data',	'RELCAPITAL_data',	'RELIANCE_data',	'RELIGARE_data',	'RELINFRA_data',	'RELMEDIA_data',	'RENUKA_data',	'REPRO_data',	'RESPONIND_data',	'RESURGERE_data',	'REVATHI_data',	'RICOAUTO_data',	'RIIL_data',	'RJL_data',	'RKFORGE_data',	'RMCL_data',	'RML_data',	'ROHITFERRO_data',	'ROHLTD_data',	'ROLTA_data',	'ROMAN_data',	'RPGLIFE_data',	'RPOWER_data',	'RPPINFRA_data',	'RSSOFTWARE_data',	'RSWM_data',	'RSYSTEMS_data',	'RUBYMILLS_data',	'RUCHIRA_data',	'RUCHISOYA_data',	'RUCHINFRA_data',	'SABERORGAN_data',	'SABTN_data',	'SADBHAV_data',	'SAGCEM_data',	'SAHPETRO_data',	'SAIL_data',	'SAKHTISUG_data',	'SAKSOFT_data',	'SAKUMA_data',	'SALORAINTL_data',	'SALSTEEL_data',	'SAMBHAAV_data',	'SAMTEL_data',	'SANDESH_data',	'SANGAMIND_data',	'SANGHIIND_data',	'SANGHVIFOR_data',	'SANGHVIMOV_data',	'SANWARIA_data',	'SARDAEN_data',	'SAREGAMA_data',	'SARLAPOLY_data',	'SASKEN_data',	'SATHAISPAT_data',	'SATYAMCOMP_data',	'SAVERA_data',	'SB&TINTL_data',	'SBBJ_data',	'SBIN_data',	'SBT_data',	'SCI_data',	'SEAMECLTD_data',	'SEINVEST_data',	'SELAN_data',	'SELMCL_data',	'SERVALL_data',	'SESAGOA_data',	'SESHAPAPER_data',	'SEZALGLASS_data',	'SGFL_data',	'SGJHL_data',	'SGL_data',	'SHAHALLOYS_data',	'SHALPAINTS_data',	'SHANTIGEAR_data',	'SHARRESLTD_data',	'SHASUNPHAR_data',	'SHILPAMED_data',	'SHILPI_data',	'SHIVAMAUTO_data',	'SHIVTEX_data',	'SHIV-VANI_data',	'SHLAKSHMI_data',	'SHOPERSTOP_data',	'SHPRE_data',	'SHREEASHTA_data',	'SHREECEM_data',	'SHREERAMA_data',	'SHRENUJ_data',	'SHREYANIND_data',	'SHREYAS_data',	'SHRIRAMCIT_data',	'SHRIRAMEPC_data',	'SHYAMTEL_data',	'SICAGEN_data',	'SICAL_data',	'SIEMENS_data',	'SIL_data',	'SILINV_data',	'SIMBHSUGAR_data',	'SIMPLEX_data',	'SIMPLEXINF_data',	'SINTEX_data',	'SIRPAPER_data',	'SITASHREE_data',	'SIYSIL_data',	'SJVN_data',	'SKFINDIA_data',	'SKMEGGPROD_data',	'SKSMICRO_data',	'SKUMARSYNF_data',	'SMARTLINK_data',	'SMLISUZU_data',	'SMPL_data',	'SMSPHARMA_data',	'SOBHA_data',	'SOFTTECHGR_data',	'SOLARINDS_data',	'SOMANYCERA_data',	'SOMATEX_data',	'SONASTEER_data',	'SONATSOFTW_data',	'SOTL_data',	'SOUTHBANK_data',	'SPANCO_data',	'SPARC_data',	'SPECTACLE_data',	'SPENTEX_data',	'SPIC_data',	'SPICEMOBIL_data',	'SPLIL_data',	'SPMLINFRA_data',	'SPYL_data',	'SREINFRA_data',	'SRF_data',	'SRGINFOTEC_data',	'SRHHLINDST_data',	'SRHHYPOLTD_data',	'SRTRANSFIN_data',	'SSWL_data',	'STAR_data',	'STARPAPER_data',	'STCINDIA_data',	'STER_data',	'STERLINBIO_data',	'STERTOOLS_data',	'STINDIA_data',	'STOREONE_data',	'STRTECH_data',	'SUBEX_data',	'SUBROS_data',	'SUDAR_data',	'SUDARSCHEM_data',	'SUJANATOW_data',	'SUJANAUNI_data',	'SUMEETINDS_data',	'SUMMITSEC_data',	'SUNCLAYTON_data',	'SUNDARAM_data',	'SUNDARMFIN_data',	'SUNDRMBRAK_data',	'SUNDRMFAST_data',	'SUNFLAG_data',	'SUNILHITEC_data',	'SUNPHARMA_data',	'SUNTECK_data',	'SUNTV_data',	'SUPERSPIN_data',	'SUPPETRO_data',	'SUPRAJIT_data',	'SUPREMEIND_data',	'SUPREMEINF_data',	'SUPREMETEX_data',	'SURAJDIAMN_data',	'SURANACORP_data',	'SURANAIND_data',	'SURANAT&P_data',	'SURYAJYOTI_data',	'SURYALAXMI_data',	'SURYAPHARM_data',	'SURYAROSNI_data',	'SUTLEJTEX_data',	'SUVEN_data',	'SUZLON_data',	'SWARAJENG_data',	'SYMPHONY_data',	'SYNCOM_data',	'SYNDIBANK_data',	'TAINWALCHM_data',	'TAJGVK_data',	'TAKE_data',	'TALBROAUTO_data',	'TALWALKARS_data',	'TANLA_data',	'TANTIACONS_data',	'TARAPUR_data',	'TATACHEM_data',	'TATACOMM_data',	'TATAELXSI_data',	'TATACOFFEE_data',	'TATAGLOBAL_data',	'TATAINVEST_data',	'TATAMETALI_data',	'TATAMOTORS_data',	'TATAPOWER_data',	'TATASPONGE_data',	'TATASTEEL_data',	'TCI_data',	'TCIDEVELOP_data',	'TCIFINANCE_data',	'TCS_data',	'TECHM_data',	'TECHNO_data',	'TECHNOFAB_data',	'TECPRO_data',	'TELEDATAIT_data',	'TEXMACOLTD_data',	'TEXMOPIPES_data',	'TFCILTD_data',	'TFL_data',	'THANGAMAYL_data',	'THEMISMED_data',	'THERMAX_data',	'THINKSOFT_data',	'THIRUSUGAR_data',	'THOMASCOOK_data',	'TI_data',	'TIDEWATER_data',	'TIIL_data',	'TIL_data',	'TIMESGTY_data',	'TIMETECHNO_data',	'TIMKEN_data',	'TINPLATE_data',	'TIPSINDLTD_data',	'TIRUMALCHM_data',	'TITAN_data',	'TNPETRO_data',	'TNPL_data',	'TNTELE_data',	'TODAYS_data',	'TOKYOPLAST_data',	'TORNTPHARM_data',	'TORNTPOWER_data',	'TRENT_data',	'TRF_data',	'TRICOM_data',	'TRIGYN_data',	'TRIL_data',	'TRIVENI_data',	'TTKHEALTH_data',	'TTKPRESTIG_data',	'TTL_data',	'TTML_data',	'TUBEINVEST_data',	'TRIDENT_data',	'TULIP_data',	'TULSI_data',	'TVSELECT_data',	'TVSMOTOR_data',	'TVSSRICHAK_data',	'TVTODAY_data',	'TWILITAKA_data',	'TWL_data',	'UBENGG_data',	'UBHOLDINGS_data',	'UCALFUEL_data',	'UCOBANK_data',	'UFLEX_data',	'UGARSUGAR_data',	'ULTRACEMCO_data',	'UMESLTD_data',	'UNICHEMLAB_data',	'UNIENTER_data',	'UNIONBANK_data',	'UNIPHOS_data',	'UNIPLY_data',	'UNITECH_data',	'UBL_data',	'UNITY_data',	'UNIVCABLES_data',	'UNITEDBNK_data',	'UPERGANGES_data',	'USHAMART_data',	'USHERAGRO_data',	'UTTAMSTL_data',	'UTTAMSUGAR_data',	'UTVSOF_data',	'VADILALIND_data',	'VAIBHAVGEM_data',	'VAKRANSOFT_data',	'VALECHAENG_data',	'VALUEIND_data',	'VARDHACRLC_data',	'VARDMNPOLY_data',	'VARUN_data',	'VARUNSHIP_data',	'VASCONEQ_data',	'VENKEYS_data',	'VENUSREM_data',	'VESUVIUS_data',	'VGUARD_data',	'VHL_data',	'VICEROY_data',	'VIDEOIND_data',	'VIJAYABANK_data',	'VIJSHAN_data',	'VIKASHMET_data',	'VIMTALABS_data',	'VINATIORGA_data',	'VINDHYATEL_data',	'VIPIND_data',	'VISAKAIND_data',	'VISASTEEL_data',	'VISESHINFO_data',	'VISHALRET_data',	'VISUINTL_data',	'VIVIMEDLAB_data',	'VLSFINANCE_data',	'VOLTAMP_data',	'VOLTAS_data',	'VSTIND_data',	'VSTTILLERS_data',	'VTL_data',	'WABAG_data',	'WABCO-TVS_data',	'WALCHANNAG_data',	'WANBURY_data',	'WEBELSOLAR_data',	'WEIZMANIND_data',	'WELCORP_data',	'WELINV_data',	'WELPROJ_data',	'WELSPUNIND_data',	'WENDT_data',	'WHEELS_data',	'WHIRLPOOL_data',	'WILLAMAGOR_data',	'WINDSOR_data',	'WINSOMYARN_data',	'WIPRO_data',	'WSI_data',	'WSTCSTPAPR_data',	'WOCKPHARMA_data',	'WWIL_data',	'WYETH_data',	'XPROINDIA_data',	'XLENERGY_data',	'YESBANK_data',	'ZANDUREALT_data',	'ZEEL_data',	'ZEELEARN_data',	'ZEENEWS_data',	'ZENITHBIR_data',	'ZENITHCOMP_data',	'ZENITHEXPO_data',	'ZENITHINFO_data',	'ZENSARTECH_data',	'ZICOM_data',	'ZODIACLOTH_data',	'ZODJRDMKJ_data',	'ZUARIAGRO_data',	'ZYDUSWELL_data',	'ZYLOG_data')
option = st.selectbox('Select dataset for prediction',dataset)
DATA_URL =('./HISTORICAL_DATA/'+option+'.csv')

year = st.slider('Year of prediction:',1,4)
period = year * 365
#DATA_URL =('./HISTORICAL_DATA/3IINFOTECH_data.csv')

@st.cache
def load_data():
    data = pd.read_csv(DATA_URL)
    data['Date'] = pd.to_datetime(data['Date'])  # Convert Date column to datetime

    # Moving Averages
    data['SMA_50'] = data['close'].rolling(window=50).mean()
    data['SMA_100'] = data['close'].rolling(window=100).mean()
    data['SMA_200'] = data['close'].rolling(window=200).mean()
    data['SMA_20'] = data['close'].rolling(window=20).mean()

    # Exponential Moving Averages
    data['EMA_50'] = data['close'].ewm(span=50, adjust=False).mean()
    data['EMA_100'] = data['close'].ewm(span=100, adjust=False).mean()
    data['EMA_200'] = data['close'].ewm(span=200, adjust=False).mean()

    # RSI Calculation
    delta = data['close'].diff(1)
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()
    rs = avg_gain / avg_loss
    data['RSI'] = 100 - (100 / (1 + rs))

    # Bollinger Bands
    data['BB_Middle'] = data['close'].rolling(window=20).mean()
    data['BB_Upper'] = data['BB_Middle'] + 2 * data['close'].rolling(window=20).std()
    data['BB_Lower'] = data['BB_Middle'] - 2 * data['close'].rolling(window=20).std()

    # MACD Calculation
    short_ema = data['close'].ewm(span=12, adjust=False).mean()
    long_ema = data['close'].ewm(span=26, adjust=False).mean()
    data['MACD'] = short_ema - long_ema
    data['Signal_Line'] = data['MACD'].ewm(span=9, adjust=False).mean()

    # Fibonacci Levels (High-Low Range)
    high = data['close'].max()
    low = data['close'].min()
    diff = high - low
    data['Fib_0.236'] = high - diff * 0.236
    data['Fib_0.382'] = high - diff * 0.382
    data['Fib_0.618'] = high - diff * 0.618

    # Support & Resistance (Using rolling max/min)
    data['Support'] = data['low'].rolling(window=20).min()
    data['Resistance'] = data['high'].rolling(window=20).max()

    # Momentum Indicator
    data['Momentum'] = data['close'] - data['close'].shift(10)

    # Ichimoku Cloud
    data['Tenkan_Sen'] = (data['high'].rolling(window=9).max() + data['low'].rolling(window=9).min()) / 2
    data['Kijun_Sen'] = (data['high'].rolling(window=26).max() + data['low'].rolling(window=26).min()) / 2
    data['Senkou_Span_A'] = ((data['Tenkan_Sen'] + data['Kijun_Sen']) / 2).shift(26)
    data['Senkou_Span_B'] = ((data['high'].rolling(window=52).max() + data['low'].rolling(window=52).min()) / 2).shift(26)

    return data


	


data_load_state = st.text('Loading data...')
data = load_data()
data_load_state.text('Loading data... done!')

def plot_fig():
	fig = go.Figure()
	fig.add_trace(go.Scatter(x=data.Date, y=data['open'], name="stock_open",line_color='deepskyblue'))
	fig.add_trace(go.Scatter(x=data.Date, y=data['close'], name="stock_close",line_color='dimgray'))
	fig.layout.update(title_text='Time Series data with Rangeslider',xaxis_rangeslider_visible=True)
	st.plotly_chart(fig)
	return fig

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)
	
# plotting the figure of Actual Data
plot_fig()

# preparing the data for Facebook-Prophet.

data_pred = data[['Date','close']]
data_pred=data_pred.rename(columns={"Date": "ds", "close": "y"})

# code for facebook prophet prediction


m = Prophet()
m.fit(data_pred)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

#plot forecast
fig1 = plot_plotly(m, forecast)
if st.checkbox('Show forecast data'):
    st.subheader('forecast data')
    st.write(forecast)
st.write('Forecasting closing of stock value for'+option+' for a period of: '+str(year)+'year')
st.plotly_chart(fig1)




def plot_sma():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.Date, y=data['close'], name="Close Price", line_color='black'))
    fig.add_trace(go.Scatter(x=data.Date, y=data['SMA_50'], name="50-Day SMA", line_color='orange'))
    
    fig.update_layout(title="Simple Moving Average", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

def plot_sma_50_100():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.Date, y=data['close'], name="Close Price", line_color='black'))
    fig.add_trace(go.Scatter(x=data.Date, y=data['SMA_50'], name="50-Day SMA", line_color='orange'))
    fig.add_trace(go.Scatter(x=data.Date, y=data['SMA_100'], name="100-Day SMA", line_color='blue'))
    
    fig.update_layout(title="50 & 100 Moving Averages", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

def plot_sma_20_100_200():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.Date, y=data['close'], name="Close Price", line_color='black'))
    fig.add_trace(go.Scatter(x=data.Date, y=data['SMA_20'], name="20-Day SMA", line_color='green'))
    fig.add_trace(go.Scatter(x=data.Date, y=data['SMA_100'], name="100-Day SMA", line_color='blue'))
    fig.add_trace(go.Scatter(x=data.Date, y=data['SMA_200'], name="200-Day SMA", line_color='red'))
    
    fig.update_layout(title="20, 100 & 200 Moving Averages", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

def plot_rsi():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.Date, y=data['RSI'], name="RSI", line_color='blue'))
    fig.add_hline(y=70, line_dash="dot", line_color="red")  # Overbought level
    fig.add_hline(y=30, line_dash="dot", line_color="green")  # Oversold level
    
    fig.update_layout(title="Relative Strength Index (RSI)", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

def plot_macd():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.Date, y=data['MACD'], name="MACD Line", line_color='purple'))
    fig.add_trace(go.Scatter(x=data.Date, y=data['Signal_Line'], name="Signal Line", line_color='red'))
    
    fig.update_layout(title="MACD (Moving Average Convergence Divergence)", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

def plot_bollinger():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.Date, y=data['BB_Middle'], name="Middle Band", line_color='black'))
    fig.add_trace(go.Scatter(x=data.Date, y=data['BB_Upper'], name="Upper Band", line_color='green'))
    fig.add_trace(go.Scatter(x=data.Date, y=data['BB_Lower'], name="Lower Band", line_color='red', fill='tonexty'))
    
    fig.update_layout(title="Bollinger Bands", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

def plot_pivot_points():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.Date, y=data['close'], name="Close Price", line_color='black'))

    # Calculating Pivot Points
    data['Pivot'] = (data['high'] + data['low'] + data['close']) / 3
    data['R1'] = (2 * data['Pivot']) - data['low']
    data['S1'] = (2 * data['Pivot']) - data['high']
    
    fig.add_trace(go.Scatter(x=data.Date, y=data['Pivot'], name="Pivot Point", line_color='orange'))
    fig.add_trace(go.Scatter(x=data.Date, y=data['R1'], name="Resistance Level 1", line_color='green'))
    fig.add_trace(go.Scatter(x=data.Date, y=data['S1'], name="Support Level 1", line_color='red'))

    fig.update_layout(title="Pivot Points (Buy/Sell Signals)", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

def plot_fibonacci():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.Date, y=data['close'], name="Close Price", line_color='black'))
    
    fig.add_trace(go.Scatter(x=data.Date, y=data['Fib_0.236'], name="Fib 23.6%", line_color='blue'))
    fig.add_trace(go.Scatter(x=data.Date, y=data['Fib_0.382'], name="Fib 38.2%", line_color='purple'))
    fig.add_trace(go.Scatter(x=data.Date, y=data['Fib_0.618'], name="Fib 61.8%", line_color='green'))

    fig.update_layout(title="Fibonacci Retracement", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

def plot_support_resistance():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.Date, y=data['close'], name="Close Price", line_color='black'))
    fig.add_trace(go.Scatter(x=data.Date, y=data['Support'], name="Support", line_color='red'))
    fig.add_trace(go.Scatter(x=data.Date, y=data['Resistance'], name="Resistance", line_color='green'))

    fig.update_layout(title="Support & Resistance Levels", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

def plot_momentum():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.Date, y=data['Momentum'], name="Momentum", line_color='blue'))

    fig.update_layout(title="Momentum Indicator", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

def plot_ichimoku():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.Date, y=data['close'], name="Close Price", line_color='black'))

    fig.add_trace(go.Scatter(x=data.Date, y=data['Tenkan_Sen'], name="Tenkan-Sen", line_color='blue'))
    fig.add_trace(go.Scatter(x=data.Date, y=data['Kijun_Sen'], name="Kijun-Sen", line_color='red'))
    fig.add_trace(go.Scatter(x=data.Date, y=data['Senkou_Span_A'], name="Senkou Span A", line_color='green', fill='tonexty'))
    fig.add_trace(go.Scatter(x=data.Date, y=data['Senkou_Span_B'], name="Senkou Span B", line_color='brown', fill='tonexty'))

    fig.update_layout(title="Ichimoku Cloud", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

st.sidebar.header("Select Indicator")
indicator = st.sidebar.selectbox(
    "Choose", 
    ["SMA", "SMA (50 & 100)", "SMA (20, 100, 200)", "RSI", "MACD", "Bollinger Bands", 
     "Pivot Points", "Fibonacci Retracement", "Support & Resistance", "Momentum", "Ichimoku Cloud"]
)

if indicator == "SMA":
    plot_sma()
elif indicator == "SMA (50 & 100)":
    plot_sma_50_100()
elif indicator == "SMA (20, 100, 200)":
    plot_sma_20_100_200()
elif indicator == "RSI":
    plot_rsi()
elif indicator == "MACD":
    plot_macd()
elif indicator == "Bollinger Bands":
    plot_bollinger()
elif indicator == "Pivot Points":
    plot_pivot_points()
elif indicator == "Fibonacci Retracement":
    plot_fibonacci()
elif indicator == "Support & Resistance":
    plot_support_resistance()
elif indicator == "Momentum":
    plot_momentum()
elif indicator == "Ichimoku Cloud":
    plot_ichimoku()









#plot component wise forecast
st.write("Component wise forecast")
fig2 = m.plot_components(forecast)
st.write(fig2)
	

	


