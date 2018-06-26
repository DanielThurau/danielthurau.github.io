---
layout: post
title: Choosing Arch over Ubuntu
---

Since I entered University freshman year (back in 2014) I've been running some form of linux on my laptop. Finally I made the jump to a DIY distro that many of you know: Arch Linux. This is going to be a multi part blog series going over my notes from the install, and what I learned.

![_config.yml]({{ site.baseurl }}/images/2018-06-25/archlinux-logo.png)

After years of distro hopping I've tried a lot of distros, from the first one my dad installed on my laptop (Ubuntu 14.04) to Mint, Centos, FreeBSD, back to Ubuntu, a failed attempt at Arch, Antergos, back to Ubuntu, and finally a fully managed and smoothly operating version of Arch, I've learned a lot about Linux and developing inside that environment... but I could never get Arch to work on my laptop. Something between partioning disks and creating EFI variables for the bootloader always tripped me up. At one point I shrugged my shoulders and found Antergos (https://antergos.com/) which is a great alternative for people in between Ubuntu and Arch, but I couldn't justify my needs for a bleeding edge rolling release environment when I was contiuously writing software for school and for my job. There was just way to many things that could go wrong, and it even failed (albeit by my hands) at the beginning of a video interview. So I slumped back to Ubuntu for reliability and universality

However, in my final weeks at Uni after turning in my last assignments I decided to give Arch the good ol' college try and... it worked! I'm unsure of how I'm going to manage the release cycle for this blog, but I'm gonna write the first part tonight. I kept a notebook, and a lot of this will be transcribing the notebook to legible reading format, and maybe an investigation into other choices and why I made my decision (based off of a 22 y/o Computer Science graduate's mind). I haven't thought through who my audience is going to be yet (i.e. do I explain things like dd or not), so that'll be up to my discretion as I write.

### Installation media and inital boot

I had to do a lot of research beforehand about machine maintenance, most importantly **systemd**. **systemd** is basically a system initalizer and service manager. It will run as PID 1 and start services listed by the kernel and by the user. It also provides users with correct privleges to manage these and new services once the system is booted. There is a lot to systemd, and its a tool that is taking over the Linux world. Its the replacement for **init** and theres a lot of controversy over it (just look at reddit and you'll already get tired of it). Pretty much if you wanna be and sysadmin at any point in your career...learn **systemd**.
