function X = dv2m(x, n)
% Data vector to data matrix
% Useful for output data matrix/vector conversion.
% 
% See also dm2v
% 
%--------------------------------------
% Author: Alexander Efremov            
% Date:   26 Apr 2009                
% Course: Multivariable Control Systems
%--------------------------------------

N = length(x)/n;
ind = ones(N, 1)*[1:n] + [0:n:N*n - 1]'*ones(1, n);
X = x(ind);
