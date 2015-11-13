function [ score ] = bcb(q,m,index,doclength)
qtok = strsplit(q,' ');
score = zeros(length(qtok));
for i = 1:length(qtok)
    %for each word in query
    current = qtok(i);
    indices = m(current{1});
    %for each doc listed in the index for that word
    tf_q = nnz(index(indices(1):indices(2)))-1;
    B =ones(indices(2)-indices(1)+1)*.5;
    %implement counts with doc # = indices, val = number of terms
    tf = [tf_q doclength(index(indices(1)+1:indices(2)+1))-tf_q];
    B = mle(tf,B,1e-5);
    %make sure this is correct in terms of element wise matrix
    score = tf-1 .* B + (tf-1)*(tf)./2.;
end
    
   
    
    
        
        
        
