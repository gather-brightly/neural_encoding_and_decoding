function [ cifti ] = ciftiopen(filename,caret7command)
%Open a CIFTI file by converting to GIFTI external binary first and then
%using the GIFTI toolbox

grot=fileparts(filename);
if (size(grot,1)==0)
grot='.';
end

tmpname = tempname;
unix([caret7command ' -cifti-convert -to-gifti-ext ' filename ' ' tmpname '.gii']);
cifti = gifti([tmpname '.gii']);
unix(['rm ' tmpname '.gii ' tmpname '.gii.data']);

end

