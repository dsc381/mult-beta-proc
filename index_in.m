doclengths = csvread('lengths',0,1);
disp('finished reading in doclength')
fid = fopen('postings_m','r');
index = spconvert(fscanf(fid,'%d %d %d',[3 Inf]).');
%index = sparse(max(A(:,1)),max(A(:,2)));
%for i= 1:size(postings_m)
%    index(A(i,1),A(i,2)) = A(i,3);
%    if mod(i,10000) == 0
%        disp(i)
%    end
%end
    
disp('finished reading in index')
disp('now sparse index')
names = read_mixed_csv('names',',',[]);
names = names(:,2);
disp('finished reading in names')

% while ischar(textLine)
% 	% get into numbers array.
% 	spltTextLine = strsplit(textLine,',');
% 	% Put numbers into a cell array IF and only if
% 	% you need them after the loop has exited.
% 	% First method - each number in one cell.
% 	% ALternate way where the whole array is in one cell.
% 	
% 	% Read the next line.
%     textLine = fgets(fid);
% 	lineCounter = lineCounter + 1;
% end
% fclose(fid);
% % Display the cell arrays in the command line.
% ca
% ca2