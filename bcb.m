qtok = strsplit(q,' ');
%move to better spot later
num_col = size(index);
tol = 1e-1;
%end
score = zeros(length(doclengths),1);
for i = 1:length(qtok)
    %for each word in query
    current = qtok(i);
    ind = m(current{1});
    %for each doc listed in the index for that word
    tf_q = (sum(index(ind(1):ind(2),:)~=0,2)-1);
    %remove CS indexing that starts at 0
    tf_q(tf_q==0) = 1;
    B =ones(ind(2)-ind(1)+1,2)*.5;
    %implement counts with doc # = indices, val = number of terms
    tf = [tf_q doclengths((index(ind(1):ind(2))+1),1)-tf_q];
    error = 1e1;
    %gradient descent for B
    while error > tol
        denom1 = psi([tf(:,1)+sum(B,2),tf(:,2)+sum(B,2)]);
        denom2 = psi(sum(B,2));
        denom3 = [denom1(:,1)-denom2,denom1(:,2)-denom2];
        B_old = B;
        B = B.*(psi(tf+B)-psi(B))./(denom3);
        error = max(abs(B-B_old));
    end
    %make sure this is correct in terms of element wise matrix
    score((index(ind(1):ind(2))+1),1) = score((index(ind(1):ind(2))+1),1) + sum((tf-1 .* B + (tf-1).*(tf)./2.))';
end
    
   
    
    
        
        
        
