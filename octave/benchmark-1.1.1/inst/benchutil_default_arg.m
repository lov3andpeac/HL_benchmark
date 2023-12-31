% Copyright (C) 2008  Jaroslav Hajek <highegg@gmail.com>
% 
% This file is part of OctaveForge.
% 
% OctaveForge is free software; you can redistribute it and/or modify
% it under the terms of the GNU General Public License as published by
% the Free Software Foundation; either version 2 of the License, or
% (at your option) any later version.
% 
% This program is distributed in the hope that it will be useful,
% but WITHOUT ANY WARRANTY; without even the implied warranty of
% MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
% GNU General Public License for more details.
% 
% You should have received a copy of the GNU General Public License
% along with this software; see the file COPYING.  If not, see
% <http://www.gnu.org/licenses/>.
% 

% benchmark_default_arg (name, value)
% set argument to a default value. This function is provided for 
% compatibility with Matlab, which misses Octave's default arguments
% feature.
%
function benchutil_default_arg (name, value)
  if (~ evalin ('caller', sprintf ('exist (''%s'', ''var'')', name)))
    assignin ('caller', name, value);
  end
