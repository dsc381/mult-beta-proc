doclengths = csvread('lengths',0,1);
scores = zeros(length(doclengths));
index = csvread('postings',0,1);
index = sparse(index);


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