queries = read_mixed_csv('test.csv',',',(1));
r_size = size(queries);
results = zeros(r_size(1),40);
for k = 1:r_size(1)
    %at the present moment, only use title queries
    q = queries{k,2};
    bcb;
    s_pos = length(find(score>0));
    [sorted, s_ind] = sort(score,'descend');
    results(k,1:min(s_pos,40)) = s_ind(1:min(s_pos,40)).';
end