% Intro Options
\ProvidesClass{plushcv}[2021/11/30 CV class]
\NeedsTeXFormat{LaTeX2e}
\DeclareOption{print}{\def\@cv@print{}}
\DeclareOption*{%
  \PassOptionsToClass{\CurrentOption}{article}
}
\ProcessOptions\relax
\LoadClass{article}

% Package Imports
\usepackage[lmargin=0.9cm, vmargin=0.85cm, rmargin=0.9cm]{geometry}
\usepackage[hidelinks]{hyperref}
\usepackage{enumitem}
\usepackage{graphicx}
\usepackage{pifont}
\usepackage[document]{ragged2e}


% Publications
\usepackage{cite}
\renewcommand\refname{\vskip -1.5cm}

% Color definitions
\usepackage[usenames,dvipsnames]{xcolor}
\definecolor{date}{HTML}{666666}
\definecolor{title}{HTML}{1D76E2}
\definecolor{primary}{HTML}{2b2b2b}
\definecolor{headings}{HTML}{6A6A6A}
\definecolor{subheadings}{HTML}{333333}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%Main Title Font Definitions
%Used for Name  and Section Headings
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%\def \pathtitlefont {fonts/sourcesanspro/} 
%\def \firstnamefont {sourcesanspro-SemiBold}
%\def \secondnamefont {sourcesanspro-light}
%\def \titlefont {\firstnamefont}
%\def \namefontsize {9.5}

%% Office Code Pro D Title:
%%%%%%%%%%%%%%%%%%%%%%%%%
% \def \pathtitlefont {fonts/officecodeprod/} 
% \def \firstnamefont {officecodeprod-medium}
% \def \secondnamefont {officecodeprod-regular}
% \def \titlefont {\firstnamefont}
% \def \namefontsize {9.5}


%% Source Sans Pro Title:
%%%%%%%%%%%%%%%%%%%%%%%%%
% \def \pathtitlefont {fonts/sourcesanspro/} 
% \def \firstnamefont {sourcesanspro-SemiBold}
% \def \secondnamefont {sourcesanspro-light}
% \def \titlefont {\firstnamefont}
% \def \namefontsize {9.5}

%% Source Serif Pro Title:
%%%%%%%%%%%%%%%%%%%%%%%%%
% \def \pathtitlefont {fonts/sourceserifpro/} 
% \def \firstnamefont {sourceserifpro-SemiBold}
% \def \secondnamefont {sourceserifpro-light}
% \def \titlefont {\firstnamefont}
% \def \namefontsize {9.5}

%% Prata Title:
%%%%%%%%%%%%%%%%%%%%%%%%%
% \def \pathtitlefont {fonts/prata/} 
% \def \firstnamefont {prata-regular}
% \def \secondnamefont {prata-regular}
% \def \titlefont {\firstnamefont}
% \def \namefontsize {9.5}

%% Marcellus Title:
%%%%%%%%%%%%%%%%%%%%%%%%%
% \def \pathtitlefont {fonts/marcellus/} 
% \def \firstnamefont {Marcellus-Regular}
% \def \secondnamefont {Marcellus-Regular}
% \def \titlefont {\firstnamefont}
% \def \namefontsize {9.5}

%% AbrilFatface Title:
%%%%%%%%%%%%%%%%%%%%%%%%%
% \def \pathtitlefont {fonts/abril_fatface/} 
% \def \firstnamefont {AbrilFatface-Regular}
% \def \secondnamefont {AbrilFatface-Regular}
% \def \titlefont {\firstnamefont}
% \def \namefontsize {9.5}

% Merriweather Title:
%%%%%%%%%%%%%%%%%%%%%%%%
 \def \pathtitlefont {fonts/merriweather/} 
 \def \firstnamefont {Merriweather-Regular}
 \def \secondnamefont {Merriweather-Light}
 \def \titlefont {\firstnamefont}
 \def \namefontsize {9.5}

%% Merriweather Title:
%%%%%%%%%%%%%%%%%%%%%%%%%
% \def \pathtitlefont {fonts/oxygen/} 
% \def \firstnamefont {Oxygen-Regular}
% \def \secondnamefont {Oxygen-Light}
% \def \titlefont {\firstnamefont}
% \def \namefontsize {9.5}

%% Inter Title:
%%%%%%%%%%%%%%%%%%%%%%%%%
% \def \pathtitlefont {fonts/inter/} 
% \def \firstnamefont {Inter-SemiBold}
% \def \secondnamefont {inter-light}
% \def \titlefont {\firstnamefont}
% \def \namefontsize {9.5}

%Main Font Definitions
\def \pathmainfont {fonts/inter/}
\def \mainfont {inter-light}
\def \mainfontbold {inter-semibold}
% \def \mainbolditalicfont {}
% \def \mainitalicfont {}
\def \mainfontsize {9.5}
\def \mainsansfont {inter-light}

%Main Subheading Font Definitions
%Used for company name and sub-skills
\def \pathsubheadingfont {\pathtitlefont}
\def \subheadingfont {\titlefont}
\def \subheadingsize {12}

%Main Job Descriptor and Location Font Definitions
%Used for company name and sub-skills
\def \pathdescriptorfont {\pathsubheadingfont}
\def \descriptorfont {\secondnamefont}
\def \descriptorsize {10}
\def \pathlocationfont {\pathsubheadingfont}
\def \locationfont {\subheadingfont}
\def \locationsize {8pt}

%Main Monospace Font Definitions 
%Used for Job Title and Contact Line 
\def \pathmonofont {fonts/officecodeprod/}
\def \monofont {OfficeCodeProD-Light}


% Set main fonts
\usepackage{fontspec}
\setmainfont[Color=primary, Path = \pathmainfont,BoldFont=\mainfontbold,UprightFeatures={SizeFeatures={Size=\mainfontsize}},
  BoldFeatures={SizeFeatures={Size=\mainfontsize}}]{\mainfont}
\setsansfont[Scale=MatchLowercase,Mapping=tex-text, Path = \pathmainfont,UprightFeatures={SizeFeatures={Size=\mainfontsize}}
  ]{\mainsansfont}

% Date command
\usepackage[absolute]{textpos}
\usepackage[UKenglish]{isodate}
\setlength{\TPHorizModule}{1mm}
\setlength{\TPVertModule}{1mm}
\newcommand{\lastupdated}{\begin{textblock}{60}(155,5)
\color{date}\fontspec[Path = \pathmainfont]{\mainfont}\fontsize{8pt}{10pt}\selectfont 
Last Updated on \today
\end{textblock}}

% Name command


\newcommand{\namesection}[4]{
\RaggedRight{
\color{title}
\fontsize{50pt}{60pt}
\fontspec[Path = \pathtitlefont]{\firstnamefont}\selectfont #1 
\fontspec[Path = \pathtitlefont]{\secondnamefont}\selectfont #2
} \\[5pt]

\noindent\makebox[\linewidth]{\color{title}\rule{\paperwidth}{0pt}}
\vspace{-15pt}

\RaggedRight{\fontspec[Path = \pathmonofont]{\monofont}\fontsize{14pt}{14pt}\selectfont #3}

\noindent\makebox[\linewidth]{\color{title}\rule{\paperwidth}{0pt}}
\vspace{-15pt}

\RaggedRight{\fontspec[Path = \pathmonofont]{\monofont}\fontsize{10pt}{14pt}\selectfont #4}

\noindent\makebox[\linewidth]{\color{title}\rule{\paperwidth}{0pt}}
\vspace{-15pt}
}

% Section separators
\usepackage{titlesec}
\titlespacing{\section}{0pt}{5pt}{5pt}
\titlespacing{\subsection}{0pt}{0pt}{0pt}
\newcommand{\sectionsep}{\vspace{5pt}}

% Headings command
\titleformat{\section}{\color{title}
\scshape\fontspec[Path = \pathtitlefont]{\titlefont}\fontsize{16pt}{24pt}\selectfont \raggedright}{}{0em}{}

% Subheadings command
\titleformat{\subsection}{
\color{subheadings}\fontspec[Path = \pathsubheadingfont ]{\subheadingfont}\fontsize{\subheadingsize}{14pt}\selectfont\bfseries\uppercase}{}{0em}{}

%Subheadings on the right
\newcommand{\runsubsection}[1]{
\color{subheadings}\fontspec[Path = \pathsubheadingfont ]{\subheadingfont}\fontsize{\subheadingsize}{14pt}\selectfont\bfseries\uppercase {#1} \normalfont}

% Descriptors command
\newcommand{\descript}[1]{
\color{subheadings}\raggedright\scshape\fontspec[Path = \pathdescriptorfont]{\descriptorfont}\fontsize{\descriptorsize}{13pt}\selectfont {#1 \\} \normalfont}

% Location command
\newcommand{\location}[1]{
\color{headings}\raggedright\fontspec[Path = \pathlocationfont]{\locationfont}\fontsize{\locationsize}{12pt}\selectfont {#1\\} \normalfont}

%Contact Line
\newcommand{\contactline}[6]{\begingroup
\setbox0=\hbox{
\includegraphics[scale=0.23,trim={0cm 1.25cm -0.4cm 0cm}]{icons/main/link.png}{#2}\hspace{0.3cm}\newline
\includegraphics[scale=0.23,trim={0cm 1.25cm -0.4cm 0cm}]{icons/main/mail.png}{#5}\hspace{0.3cm}
\includegraphics[scale=0.23,trim={0cm 1.25cm -0.4cm 0cm}]{icons/main/phone.png}{#6}
}\parbox{\wd0}{\box0}\endgroup}

%Inline Centered Logo
\newcommand{\vcenteredinclude}[2]{\begingroup
\setbox0=\hbox{\includegraphics[scale=0.10,trim={0 0.7cm 0cm 0cm}]{#1} {#2}}
\parbox{\wd0}{\box0}\endgroup}


% Bullet Lists with fewer gaps command
\newenvironment{tightemize}{
\vspace{-\topsep}\begin{itemize}[label=\ding{212}]\itemsep1pt \parskip0pt \parsep0pt}
{\end{itemize}\vspace{-\topsep}}

