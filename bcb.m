qtok = strsplit(q,' ');
%move to better spot later
num_col = size(index);
tol = 1e-3;
%end
score = zeros(length(doclengths),1);
for i = 1:length(qtok)
    %for each word in query
    current = qtok(i);
    if ~isKey(m,current{1}) %make sure q term is in corpus
        continue
    end
    ind = m(current{1});
    %for each doc listed in the index for that word
    tf_q = (sum(index(ind(1):ind(2),:)~=0,2)-1);
    %remove CS indexing that starts at 0
    tf_q(tf_q<=0) = 1;
    %I suck at matlab and can't do this cleaner
    B =ones(ind(2)-ind(1)+1,2)*.5;
    %implement counts with doc # = indices, val = number of terms
    tf = [tf_q doclengths((index(ind(1):ind(2))+1),1)-tf_q];
    error = [10 10];
    prev = [0 0];
    a = 0.003;
    %gradient descent for B
    while max(error > tol)
        prev = error;
        %# old approach using upper bound
        %denom = [(psi(sum(tf,2)+sum(B,2)) - psi(sum(B,2))), (psi(sum(tf,2)+sum(B,2)) - psi(sum(B,2)))];
        gl = psi(sum(B,2))-psi(sum(tf,2)+sum(B,2));
        B_old=B;
        B = B + a *([gl gl] + psi(tf+B) - psi(B));
        %# old approach using upper bound
        %B = B.*(psi(tf+B)-psi(B))./denom;
        error = max(B-B_old);
    end
    %make sure this is correct in terms of element wise matrix
    score((index(ind(1):ind(2))+1),1) = score((index(ind(1):ind(2))+1),1) + sum((tf-1 .* B + (tf-1).*(tf)./2.),2);
end
    
   
    
    
        
        
        
