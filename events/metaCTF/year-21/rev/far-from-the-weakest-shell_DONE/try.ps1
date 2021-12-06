# Set-Variable -Name nU0 -Value ([typE]("{4}{2}{5}{0}{6}{1}{3}{10}{9}{8}{7}"-f 'TY.CrYP','ogrAp','ystEm','H','s','.seCUrI','T','oRIThM','Alg','h','y.hAs'))  

Set-Variable -Name nU0 -Value [type]System.Security.Cryptography.HashAlgorithm

# Set-Variable -Name Clob -Value ([TyPe]("{4}{5}{3}{0}{2}{1}"-F'OnV','r','eRtE','tc','SysteM.b','i')) 

Set-Variable -Name Clob -Value [type]System.BitConverter

# SET-iTeM  vaRiabLe:OMz  (  [tYPE]("{1}{0}{2}" -f'con','SYSTEM.','vERT'))

Set-Variable -Name OMz [type]System.Convert

# SEt-ITEM vARIABlE:pO52Ew ([typE]("{1}{4}{2}{3}{0}"-F'Ng','sYstEM','t.eNc','OdI','.teX')  ) 

Set-Variable -Name pO52Ew [type]System.Text.Encoding

# sEt-itEm  ('va'+'ria'+'BLE:'+'2L36D')  (  [typE]("{0}{1}"-F'sTrin','G'))  

Set-Variable -Name 2l36d [type]String

function wFKh(${STR}) {
	# Set-Variable -Name SBvn -Value ((  VaRIAbLe  ('nU'+'0') ).vAlUE::("{0}{1}"-f'Creat','e').Invoke(("{2}{0}{1}" -f'a25','6','sh')))

    # Set-Variable -Name sbvn -Value System.Security.Cryptography.HashAlgorithm.value::Create.Invoke(sha256)

	# Set-Variable -Name gchekrns -Value (${SbVn}."COMpUTehASH"( ( ls VaRIAblE:Po52ew ).Value::"uTF8".("{0}{1}" -f 'GetB','ytes').Invoke(${STr})))
	# Set-Variable -Name ANVI -Value ($CLOB::("{2}{1}{0}" -f'g','Strin','To').Invoke(${gCheKrNs}))

	# return ${anVI}.("{1}{0}{2}" -f 'c','Repla','e').Invoke('-', '')
    return [System.BitConverter]::ToString([System.Security.Cryptography.HashAlgorithm]::Create("sha256").ComputeHash([System.Text.Encoding]::UTF8.GetBytes(${Str}))).replace('-','')
}

function yuFAs(${BsNz}, ${wcin}) {
	Set-Variable -Name uRcnB -Value (&("{0}{1}{2}"-f 'Ge','t','-Item') ${BSnZ})
	foreach(${_} in ${URcNB}.("{0}{1}{2}"-f 'G','etSubkeyName','s').Invoke()){ 
		Set-Variable -Name NaMe -Value (${URCnB}."NAmE" + "\" + ${_})
		Set-Variable -Name GcHEKRNS -Value (.("{1}{0}" -f'fkh','w') ${NAMe})
		if(${wCIN} -eq ${gchEkRNS}){
			return &("{1}{0}" -f'h','wfk') ${_}
		}
	}
	return ("{0}{1}"-f 'N','OPE!')
}

function v1(${In}) {
    # Set-Variable -Name keY -Value (&("{0}{1}" -f 'yu','fas') ((("{4}{2}{1}{3}{0}" -f 's','TWA','M:dQUSOF','REdQUClasse','HKL'))."ReplAcE"('dQU',[stRInG][cHar]92)) ("{4}{12}{5}{2}{3}{7}{9}{15}{10}{6}{11}{0}{14}{8}{19}{17}{1}{18}{16}{13}"-f'EE9D','92C','CAF12F','68','E','ECC8','DE5','B064E','166AA','AC31','F531','B00A2','8','C0','F2','4','F5','1','F29B6','5724'))

    $key = yufas("HKLM:\SOFTWARE\Classes", "E8ECC8CAF12F68B064EAC314F531DE5B00A2EE9DF2166AA5724192CF29B6F5C0")
    $key = wfkh('txtfile')

    # Set-Variable -Name Key -Value (( variablE  ("O"+"MZ")).vAlue::"tOBAse64sTRINg"(  ( gEt-cHIldItEM ("varIa"+"bl"+"E:P"+"O52E"+"W")  ).VaLue::"uTF8".("{0}{1}" -f'G','etBytes').Invoke(${kEy})))

    $key = [System.Convert]::ToBase64String(Get-ChildItem [System.Text.Encoding]::UTF8.GetBytes(${key}))

    Set-Variable -Name CODE -Value (@(-7, -39, -16, 18, -12, 0, 7, -34, -5, -62, -38, -11, 1, -3, -17, -53, -18, -19, 46, 58))
    Set-Variable -Name iN -Value ((  geT-cHilDIteM  VariablE:oMZ).vaLuE::"TObaSE64StRing"(  (VAriable PO52eW -vAl )::"uTF8".("{0}{1}{2}"-f'G','etB','ytes').Invoke(${IN})))
    Set-Variable -Name iN -Value (${iN}[0 .. ${iN}."LENGTh"])
    foreach(${I} in (0 .. (${iN}."lENgTH" - 1))){
        ${In}[${I}] = [char]([Int]([char]${iN}[${I}]) + ${COdE}[${i}])
        if (${in}[${i}] -ne ${key}[${i}]){
            return ${FALse}
        }
    }
    return ${TrUe}
}

function v2(${IN}) {
    Set-Variable -Name keY -Value (.("{1}{0}"-f 'ufas','y') ((("{3}{2}{4}{0}{5}{1}"-f 'SOFTWARE','TKClasses','T','HKLM:P','K','P')) -crePLAce([ChAr]80+[ChAr]84+[ChAr]75),[ChAr]92) ("{5}{3}{16}{10}{17}{7}{19}{1}{9}{12}{2}{13}{8}{0}{6}{14}{11}{15}{18}{4}" -f '4','9','B','F0B','1','7D','111','F','2','A','953BAF801F','F','C','A485','6','6CBD36CE','C456','DF5703C0','1','DB2A73A1759'))
    Set-Variable -Name Key -Value ((GEt-varIABle ('O'+'mz') -VAluEo )::"TOBaSe64sTRing"( $Po52eW::"utF8".("{1}{2}{0}" -f 's','G','etByte').Invoke(${KEy})))
    Set-Variable -Name COde -Value (@(-6, 20, -35, -17, -7, -1, -21, -49, 6, 1, -8, -33, -18, -3, -23, -56, -11, 3, 5, 7))
    Set-Variable -Name iN -Value ((VaRiAbLE OMz -Va)::"TOBAsE64stRING"( ( varIablE  ('Po'+'5'+'2eW') -VALU)::"uTf8".("{0}{1}{2}" -f'Ge','tBy','tes').Invoke(${In})))
    Set-Variable -Name In -Value (${iN}[0 .. ${In}."leNgTh"])
    foreach(${i} in (0 .. (${IN}."lenGTh" - 1))){
        ${in}[${i}] = [char]([System.Int32]([char]${IN}[${I}]) + ${cODE}[${i}])
        if (${in}[${i}] -ne ${KEy}[${i}]){
            return ${fALSE}
        }
    }
    return ${TrUe}
}

function V3(${IN}) {
    Set-Variable -Name kEY -Value (&("{0}{1}"-f'yufa','s') ((("{3}{4}{1}{5}{2}{0}"-f 'EvldClasses',':vldSO','AR','HKL','M','FTW'))  -cREpLacE'vld',[CHAr]92) ("{10}{15}{4}{7}{16}{3}{6}{8}{0}{14}{2}{5}{13}{1}{12}{11}{9}{17}"-f'4BAAB1','B','7024','144D8','BB','A','1A9','AA97ECB3DE22A3','3B','4','8E0F76163','1F','7','E','6B21','2547D','41','2'))
    Set-Variable -Name key -Value ((varIaBlE  oMz -vAluE  )::"tObAse64STrING"(  $Po52ew::"utF8".("{2}{0}{1}"-f 'Byt','es','Get').Invoke(${keY})))
    Set-Variable -Name cODe -Value (@(-20, 35, -5, 0, -11, -20, 29, -52, -17, 52, 9, 3, 4, -15, -13, 35, -24, -33, 28, 61))
    Set-Variable -Name IN -Value ((gET-item  VARIaBlE:OmZ  ).valUe::"TObasE64sTRIng"( (Get-VaRIaBlE  Po52ew  ).VAluE::"uTF8".("{0}{1}{2}" -f'G','etB','ytes').Invoke(${IN})))
    Set-Variable -Name in -Value (${iN}[0 .. ${iN}."lenGth"])
    foreach(${I} in (0 .. (${IN}."LengTh" - 1))){
        ${IN}[${i}] = [char]([System.Int32]([char]${IN}[${i}]) + ${coDe}[${I}])
        if (${iN}[${i}] -ne ${kEy}[${i}]){
            return ${FALsE}
        }
    }
    return ${TRUE}
}

Set-Variable -Name INPUT -Value (Read-Host Please enter the flag to receive your flag)

if (${iNPUT}."leNGTh" -eq 39) {
    ${part1} =   $2l36d::"JoIN"("", ${iNPUT}[ 0..12])
    ${part1} =   (  GeT-vaRiaBLE ("2l3"+"6d") -valUeoNlY )::"jOiN"("", ${inPUt}[13..25])
    ${part3} =  (  Gci  ('VA'+'riA'+'blE:'+'2l36D') ).vaLue::"jOIN"("", ${INpUt}[26..39])
    if ((.('v1') ${part1}) -and (&('v2') ${part2}) -and (.('v3') ${part3})) {
        Write-Host "You've clearly already got the flag, so why even ask?"
    } else {
        Write-Host No flag for you.
    }
} else {
    Write-Host No flag for you
}

