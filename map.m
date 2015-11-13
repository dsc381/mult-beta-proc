fid = fopen('postings');
tline = fgetl(fid);
current = '.';
m = containers.Map;
beginning = false;
id = 1;
while ischar(tline)
    word = textscan(tline,'%s','delimiter',',');
    if ~strcmp(current,word{1}{1})
        if beginning
            current = word{1}{1};
            beginning = false;
            start = id-1;
        else
            fin = id-1;
            beginning = true;
            m(current)=[start fin];
        end      
    end
    id = id+1;
    tline = fgetl(fid);
end 