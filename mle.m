function [ B ] = mle(X,B,tol)

%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
error = 1e1;
while error > tol
    B = B.*(psi(X+B)-psi(B))./(psi(x*sum(B)) - psi(B));
    error = min(B);
end
end


