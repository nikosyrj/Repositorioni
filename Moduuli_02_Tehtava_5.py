leiviskat = int(input("Anna leiviskät: "))
naulat = int(input("Anna naulat: "))
luodit = int(input("Anna luodit: "))

luodit_yht = leiviskat * 20 * 32 + naulat * 32 + luodit
grammat = luodit_yht / 13.3
kilot = int(grammat // 1000)
grammat_jaljella = grammat % 1000

print(f"Massa nykymittojen mukaan: {kilot} kg ja {grammat_jaljella:.2f} g")