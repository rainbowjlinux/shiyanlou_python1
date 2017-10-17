set nu
set smartindent
set autoindent
filetype indent on
set smartcase
set showmatch
set expandtab
set tabstop=4
set shiftwidth=4
set mouse=a
au BufReadPost * if line("'\"") > 0|if line("'\"") <= line("$")|exe("norm '\"")|else|exe "norm $"|endif|endif
