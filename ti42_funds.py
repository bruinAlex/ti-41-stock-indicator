import yfinance as yf
import pandas as pd
import datetime 

today = datetime.date.today()
tomorrow = today + datetime.timedelta(days = 1)
today_minus_100 = today - datetime.timedelta(days=100)

# etf_list = ['SPY', 'IVV', 'VOO', 'VTI', 'QQQ', 'AGG', 'VEA', 'IEFA', 'GLD', 'VWO', 'BND', 'EFA', 'IEMG', 'VTV', 'IWF', 'VUG', 'LQD', 'VIG', 'IJH', 'IWD', 'USMV', 'IJR', 'IWM', 'VNQ', 'VCIT', 'BNDX', 'VO', 'VYM', 
# 'XLK', 'SHV', 'SHY', 'VGT', 'IVW', 'VCSH', 'BSV', 'ITOT', 'MBB', 'IEF', 'VB', 'IAU', 'VEU', 'EEM', 'TIP', 'XLV', 'BIL', 'DIA', 'IWB', 'TLT', 'SCHF', 'GOVT', 'SCHX', 'QUAL', 'VXUS', 'IWR', 'IXUS', 'MUB', 
# 'XLF', 'HYG', 'IVE', 'VV', 'SDY', 'PFF', 'SCHB', 'XLP', 'IGSB', 'DVY', 'MDY', 'MINT', 'EMB', 'IEI', 'VT', 'BIV', 'VMBS', 'GDX', 'ACWI', 'RSP', 'EFAV', 'VBR', 'XLY', 'VGK', 'XLU', 'SCHD', 'IWP', 'JPST', 
# 'SPLV', 'DGRO', 'VHT', 'EWJ', 'SCHP', 'IWS', 'IWV', 'SCHG', 'MTUM', 'XLE', 'IGIB', 'FVD', 'FLOT', 'JNK', 'SCZ', 'VGSH','VBK', 'SCHZ', 'VOE', 'XLI', 'IUSG', 'FDN', 'SCHO', 'GSLC', 'IWO', 'XLC', 'IBB', 'VTIP', 
# 'VTEB', 'IWN', 'SCHA', 'VXF', 'NEAR', 'SLV', 'SPYG', 'VOT', 'HDV', 'VGIT', 'SPSB', 'IUSV', 'SCHV', 'EWZ', 'SCHE', 'IJK', 'NOBL', 'VFH', 'MGK', 'MCHI', 'SPDW', 'LMBS', 'ACWV', 'OEF', 'PGX', 'FNDX', 'SCHM', 'SPAB', 
# 'SCHR', 'VDC', 'FTSM', 'SPIB', 'BLV', 'SCHH', 'IUSB', 'FPE', 'IHI', 'EFV', 'IYW', 'VSS', 'VNQI', 'FXI', 'IJS', 'USHY', 'EEMV', 'FNDF', 'EFG', 'EZU', 'EWY', 'DBEF', 'PRF', 'USIG', 'IJJ', 'SPLG', 'VCLT', 'SHM', 
# 'ESGU', 'GDXJ', 'VPU', 'BKLN', 'FTCS', 'GBIL', 'SHYG', 'SPYV', 'ISTB', 'CWB', 'IJT', 'AAXJ', 'TFI', 'HYLB', 'XBI', 'IDV', 'AMLP', 'VONG', 'SPEM', 'EMLC', 'VLUE', 'ACWX', 'IGV', 'IEUR', 'EWT', 'IYR', 'GUNR', 
# 'TOTL', 'VOOG', 'FNDA', 'FTEC', 'VPL', 'BBCA', 'BOND', 'SUB', 'DGRW', 'SPTM', 'IXN', 'ITA', 'HYD', 'FLRN', 'IGF', 'XLRE', 'USO', 'INDA', 'SJNK', 'SPTS', 'PCY', 'ICSH', 'MOAT', 'PTLC', 'DON', 'XMLV', 'VIS', 
# 'SPHD', 'BBJP', 'IDEV', 'VDE', 'KWEB', 'MGV', 'HEFA', 'GVI', 'GSY', 'VCR', 'HEDJ', 'XLB', 'IAGG', 'SOXX', 'FNDE', 'BBEU', 'SKYY', 'MGC', 'ONEQ', 'VONV', 'ARKK', 'VGLT', 'QTEC', 'STIP', 'IYH', 'RODM', 'SPTL', 
# 'ESGE', 'SPMB', 'XT', 'RPG', 'IXJ', 'SLQD', 'SCHC', 'DLN', 'PZA', 'IOO', 'EWG', 'GLDM', 'USFR', 'EMLP', 'EWC', 'IGLB', 'SMH', 'REET', 'IGM', 'ASHR', 'BSCL', 'VOX', 'IWY', 'ICF', 'PDBC', 'DEM', 'BSCM', 'SLYV', 
# 'DXJ', 'SPIP', 'EWU', 'FIXD', 'FV', 'SUSL', 'SPTI', 'XOP', 'ESGD', 'ITM', 'DSI', 'SPMD', 'SPYD', 'FNDC', 'VIGI', 'EPP', 'SPHQ', 'FEZ', 'RWO', 'FXL', 'BSCK', 'SGOL', 'USSG', 'FBT', 'GEM', 'ANGL', 'RWR', 'FHLC', 
# 'FXH', 'SPSM', 'EDV', 'VWOB', 'XSLV', 'FTSL', 'RYT', 'FMB', 'NFRA', 'MDYG', 'GSIE', 'PGF', 'VRP', 'IBDM', 'FLQL', 'SLYG', 'VNLA', 'EWH', 'CMF', 'SRLN', 'VAW', 'BAB', 'USMC', 'DES', 'USRT', 'QDF', 'AOR', 'DGS', 
# 'FDL', 'XAR', 'EWL', 'CIBR', 'JHMM', 'JKE', 'PRFZ', 'GXC', 'IEV', 'TLH', 'HYLS', 'RWX', 'PDP', 'DLS', 'IYF', 'SUSA', 'VTWO', 'CWI', 'HACK', 'IBDN', 'TILT', 'MDYV', 'IBDL', 'HYS', 'VONE', 'IQLT', 'AOM', 'VYMI', 
# 'TDTT', 'AIA', 'BSCN', 'BBAX', 'BOTZ', 'ESGV', 'FBND', 'IYY', 'SDOG', 'PXH', 'SIZE', 'VOOV', 'PXF', 'UUP', 'RDVY', 'AGGY', 'FPX', 'TDIV', 'PSK', 'KRE', 'KBE', 'IBDO', 'OMFL', 'ROBO', 'EWA', 'BSJL', 'PHO', 
# 'JPIN', 'BWX', 'PULS', 'HYMB', 'AOA', 'SLY', 'QYLD', 'FEX', 'IPAC', 'EBND', 'RSX', 'BSJK', 'SCHK', 'BSCO', 'BBRE', 'FLCB', 'XLG', 'IDU', 'XSOE', 'CLTL', 'IDLV', 'ILF', 'IYG', 'BAR', 'IGOV', 'DBC', 'INTF', 
# 'AGZ', 'LGLV', 'GNR', 'IHF', 'URTH', 'FXU', 'FTC', 'QAI', 'FUTY', 'JHML', 'MNA', 'IBDP', 'RDIV', 'VIOO', 'LRGF', 'IVOO', 'VSGX', 'PKW', 'IYC', 'QLTA', 'ITB', 'IXC', 'KXI', 'DHS', 'RWL', 'LVHD', 'JKD', 'PTNQ', 
# 'PWV', 'STPZ', 'FREL', 'PPA', 'FNCL', 'CQQQ', 'QQEW', 'DTD', 'RYH', 'JHEM', 'PCEF', 'CFA', 'PFXF', 'HTRB', 'PFFD', 'BSJM', 'QUS', 'IYJ', 'GDVD', 'PEY', 'KSA', 'JPUS', 'FTA', 'TLTD', 'IHDG', 'KIE', 'CORP', 'AOK', 
# 'DWX', 'DWM', 'EPI', 'REGL', 'GWX', 'DVYE', 'CGW', 'CFO', 'PWB', 'EZM', 'FXO', 'IVOG', 'FSTA', 'TFLO', 'FLCO', 'EWQ', 'PTMC', 'FDIS', 'PHB', 'PPLT', 'IWC', 'IBDQ', 'SMDV', 'CDC', 'REM', 'JKG', 'GLTR', 'ICLN', 'TDTF']

four_01k_list = ['DFCEX', 'DODGX', 'PMEGX', 'VFWSX', 'VMFXX', 'VWILX', 'VBITX', 'SPY', 'TQQQ']

results = {}

test_ticket = etf_list[0]
def ti42(ticker, tomorrow, today_minus_100):
	etf_df = yf.download(ticker, 
						start=today_minus_100.strftime("%Y-%m-%d"), 
						end=tomorrow.strftime("%Y-%m-%d"), 
						progress=False)
	sma_4 = etf_df.iloc[-4:, 3].mean() # last 4 rows, 3 == 'Close' col
	sma_42 = etf_df.iloc[-42:, 3].mean()

	# print(f"sma_4: {sma_4}, sma_42: {sma_42}, ti42: {sma_4/sma_42}")

	return sma_4 / sma_42 * 100

for fund in four_01k_list:
	results[fund] = ti42(fund, tomorrow, today_minus_100)


results_df = pd.DataFrame.from_dict(results, orient='index')
results_df = results_df.sort_values(by=0, ascending=False)
results_df.columns = ["TI42"]

print(f"As of: {today}")
print(results_df)
# if __name__ == '__main__':
# 	main()