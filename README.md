# Log-Analysis-project-:
### by varshini

## What is log analysis
`log analysis (or system and network log analysis) is an art and science seeking to make sense out of computer-generated records (also called log or audit trail records)
  It prints the most popular articles?
  Print the most popular article authors?
  On which days did more than 1% of requests lead to errors?`
 
 ## Software Requirements
 > `python3` - It is a general-purpose interpreted, interactive, object-oriented, and high-level programming language.
 > `Git-Bash` - Git is a distributed version-control system for tracking changes in source code.
 > `Virtual-Box` - Oracle VM VirtualBox is a free and open-source hosted hypervisor.
 > `Vagrant` - It is an open-source softwarw product for building and maintaining portable virtual software development environmeants.
 > `PostgreSQL` - It is an object-relational database system that uses and extendds the SQL language combined with many features that safely.
 > `Any Editor` - Like (Sublime text, Notepad, Notepad++, Visual Studio)

## Donwload Links
 
 | Softwares | Links |
 | ------------ | ----- |
 | Python3 | [https://www.python.org/downloads/] |
 | Git-Bash | [https://git-scm.com/downloads] |
 | Virtual-Box | [https://www.virtualbox.org/wiki/Downloads] |
 | Vagrant | [https://www.vagrantup.com/downloads.html] |
 | PostgreSQL | [https://www.enterprisedb.com/downloads/postgres-postgresql-downloads] |
 | Sublime text | [https://www.sublimetext.com/3] |

 ## procedure for project execution
>Follw these steps-:
> You must install above links.
> 1.Click on clone or download.
> 2.Extract the file.
> 3.Past the download file near the database folder.
> 4.Download database from here. --> [download-database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

## How to run Log-Analysis-Project

 * First place the all files in `vagrant` folrder
 * Click on right button.
 * Open `gitbash` here.

##commands for execution (sequential order)
```sh
vagrant up
```
```sh
vagrant ssh
```
```sh
cd /vagrant
```
```sh
cd "folder name"
```
```sh
ll or ls (for checking the subfolder inside root folder)
```
```sh
psql -d news -f newsdata.sql   (compulsory command )
```
```sh
python filename.py
```

#### Note-: Queries takes some time to run.

