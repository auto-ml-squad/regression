function Pm = mdstdn(Pm, st)
% Model destandardization
% Applicable for parameter matrix representation. 
% If standardized model is in parameter vector form, 
% then before MDSTDN use 
%     Pm = pv2m(pm, na, nb);
% before to use 
%     Pm = mdstdn(Pm, na, nb, st)
% 
% See also STDN
% 
%--------------------------------------
% Author: Alexander Efremov            
% Date:   26 Apr 2009                  
% Course: Multivariable Control Systems
%--------------------------------------

mf = st.mf;
my = st.my;
Sf = diag(st.stdf);
Sy = diag(st.stdy);
% Destandardization
Pm = Sf^-1*Pm*Sy;
Pm = [my' - mf'*Pm; Pm];
