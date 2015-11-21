function [indices] = inds(index,ind,mode)
if strcmp(mode,'tf')
    indices = zeros(ind(2)-ind(1),1);
    k = 1;
    for i=ind(1):ind(2)
        indices(k,1) = sum(index(index(:,1) == i,3).' ~= -1);
        k = k+1;
    end
end
if strcmp(mode,'doc')
    indices = index( ind(1) <=index(:,1) & index(:,1) <= ind(2) & index(:,2) == 1,3)+1;
end


