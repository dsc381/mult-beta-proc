queries = read_mixed_csv('rob04.titles.tsv_m',',',(1));
r_size = size(queries);
results = zeros(r_size(1),40);
    disp(k)
    %at the present moment, only use title queries
    q = 'when';
    bcb;
    s_pos = length(find(score>0));
    [sorted, s_ind] = sort(score,'descend');
    results(k,1:min(s_pos,40)) = s_ind(1:min(s_pos,40)).'-1;
output = [cell2mat(queries(:,1)), results];
dlmwrite('matlab_output.csv',output);