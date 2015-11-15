fid = fopen('postings');
tline1 = fgetl(fid);
tline2 = fgetl(fid);
m = containers.Map;
id = 1;
fin_id = 0;
start= id;
while ischar(tline2)
    word1 = textscan(tline1,'%s','delimiter',',');
    word2 = textscan(tline2,'%s','delimiter',',');
    fin_id = fin_id + 1;
    start = id;
    if strcmp(word1{1}{1},word2{1}{1})
        tline1 = tline2;
        tline2 = fgetl(fid);
        continue
    end
    id = fin_id+1;
    fin = fin_id;
    m(word1{1}{1}) = [start fin];
    

    tline1 = tline2;
    tline2 = fgetl(fid);
end
m(word1{1}{1}) = [start fin_id+1];
