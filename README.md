<<<<<<< HEAD
## Съдържа кода от MATLAB написан на Python и две Jupyter Notebooks които съдържат повече информация за използваните данни.

### MATLAB :arrow_right: Python
:ballot_box_with_check: **main_lspm** -  достигат се същите резултати като в Matlab. 

:ballot_box_with_check: **main_lspv** - достигат се същите резултати като в Matlab. 

:ballot_box_with_check: **main_roblspm** - достигат се същите резултати като в Matlab. 

:ballot_box_with_check: **main_roblspv** - достигат се същите резултати като в Matlab. 

:ballot_box_with_check: **main_wlspv** - достигат се същите резултати като в Matlab. 

:ballot_box_with_check: **main_elspm** - достигат се същите резултати като в Matlab. 

:x: **main_elspv** - алгоритъмът в Matlab използва разредени матрици и не получава същите резултати при използването на пълни матрици. В Numpy не съм намерил подходящи команди за използване на такива разредени матрици, и затова не мога да пренапиша тази ф-я в Python.

---
:warning: **Допълнителни файлове** - почти всички (без тези използвани само от main_elspv) са пренаписани на Python. Нужно е допълнително изчистване и подреждане на кода и добавяне на ясни и смислени коментари за повече яснота при използване на кода.
=======
# regression
Multivariable System Identification

The goal of the project is to developed in Python different parameter estimators of dynamic multiple input multiple output (MIMO) regression models in parameter matrix (PM) and in parameter vector (PV) form.

The following estimators are developed in Matlab:  <br>
	lspm.m		- Least Squares (LS) for models in PM form <br>
	lspv.m		- LS for models in PV form <br>
	elspm.m		- Extended LS (ELS) for models in PM form <br>
	elspv.m		- ELS for models in PV form <br>
	roblspm.m	- Robust LS (RobLS) for models in PM form <br>
	roblspv.m	- RobLS for models in PV form <br>
	wlspv.m		- Weighted LS (WLS) for models in PV form <br>
<p>
This code is used as benchmark for the development in Python. Also, the estimators: <br>
	wlspm.m 	- WLS for models in PM form <br>
	ivpm.m		- Instrumental Variable (IV) for models in PM form <br>
	ivpv.m		- IV  for models in PV form <br>
	other estimators... <br>
are still not developed in matlab but should be written in Python.
<p>
Additionally for testing purposes are created the following Matlab scripts <br>
	main_lspm.m <br>
	main_lspv.m <br>
	main_elspm.m <br>
	main_elspv.m <br>
	main_roblspm.m <br>
	main_roblspv.m <br>
	main_wlspv.m <br>
<p>
The main scripts: <br>
	main_lspm.m <br>
	main_ivpm.m <br>
	main_ivpv.m <br>
	other scripts for testing... <br>
are still not developed in Matlab but should be written in Python. <br>
>>>>>>> 0cf0d1aa2f058fdc0d881fad86195c37539fc0fd
