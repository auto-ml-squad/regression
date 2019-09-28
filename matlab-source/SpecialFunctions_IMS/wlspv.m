function mod = wlspv(U, Y, W, par)
% WLSPV calculates Weighted Least Squares (LS) estimates
% of ARX model in parameter vector form.
% In case of static model factors are in matrix U and Y = [].
% [pm, F] = lspv(U, Y, W, par) determines the LS-estimates of ARX model
%    A(q^-1)*yk = B(q^-1)*uk + ek
% represented in a parameter vector form is
%    yk = Fk*pm + ek,
% where:
%    A(q^-1) is [el x el] polynomial matrix with elements
%       aij(q^-1) = aij0 + aij,1*q^-1 + ...  + aij,naij*q^-naij 
%    B(q^-1) is [el x m] polynomial matrix
%       bij(q^-1) = 0 + bij,1*q^-1 + ...  + bij,nbij*q^-nbij 
%    na and nb are matrices of pollynomials' degrees with elements
%    naij - degree of polynomial aij(q^-1) and nbij - degree of bij(q^-1)
%    k - current time instant
%    uk - input vector in k-th time instant
%    yk - output vector in k-th time instant
%    ek - residual vector in k-th time instant 
%    Fk - [el x p] regression matrix in the k-th time instant with
%       p = sum(sum(na)) + sum(sum(nb))
%    pm is vector of model parameters
% 
% Inputs: 
%   U - [N x m] input data matrix with structure
%       U = [u1 u2 ... uN]'
%       where N is the length of the observation interval
%   Y - [N-n x el] output data matrix with structure
%       Y = [y1 y2 ... yN]',
%   W - [N-n x el] weight data matrix with structure
%       W = [w1 w2 ... wN]',
%   par - structure with fields:
%     na - [el x el] matrix containing the degrees of the polynomials in
%       A(q^-1) /na(i, j) is the degree of aij(q^-1)/
%     nb - [el x m] matrix containing the degrees of the polynomials in
%       B(q^-1) /nb(i, j) is the degree of bij(q^-1)/
%
% Outputs: 
%    pm - [p x 1] vector, containing estimates of model parameters
%
% See also LSPM
% 
%--------------------------------------
% Author: Alexander Efremov            
% Date:   26 Apr 2009                  
% Course: Multivariable Control Systems
%--------------------------------------

% if nargin == 3, pm = (U'*U)^-1*U'*Y;  return,  end % static system

if ~isfield(par, 'mtype'), par.mtype = 'sparse'; end
if ~isfield(par, 'intercept'), par.intercept = 0; end

r = size(Y, 2);
na = par.na;
nb = par.nb;
n = max(max([na nb]));

% Data matrix
F = dmpv(U, Y, par);

% LS
if n == 0,  pm = [];  return,  end
if exist('W', 'var'), 
   if isequal(par.mtype, 'sparse')
      if r > size(W, 2),   W = sparse(diag(repmat(W(n + 1:end), r, 1)));
      else                 W = sparse(diag(vec(W(n + 1:end))));
      end
   else
      if r > size(W, 2),   W = diag(repmat(W(n + 1:end), r, 1));
      else                 W = diag(vec(W(n + 1:end)));
      end
   end
   pm = full(F'*W'*F)^-1*F'*W*vec(Y(n + 1:end, :)');
else
   pm = (F'*W*F)^-1*F'*W*vec(Y(n + 1:end, :)');
end
mod.pm = full(pm);
mod.par = par;

