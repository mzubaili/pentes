ó
Mð[c           @   s   d  d l  Z  d  d l Z d  d l Z d  d l Z d Z d Z d Z d Z d Z d   Z	 d   Z
 d	   Z d
   Z d   Z e   e	   e   d S(   iÿÿÿÿNs   [1;31ms   [1;32ms   [1;33ms   [1;36ms   [0mc           C   s	   d GHd  S(   Ns2  [1;33m
_____  ___ ___   _____ ___ ____ _____ ___ ___  
|    \ |   | | |   |   |   |      |   |   |  \ 
|____/ |__ | | |   |   |__ |___   |   |__ |__/ 
|      |   | | |   |   |      |   |   |   | \  
|      |__ | |_|   |   |__ ___|   |   |__ |  \ 

                                 [1;31mBy: [0mAnonyMass(    (    (    (    s	   pentes.pyt   logo   s    c    
      C   s)  d }  d } d } d } d } d } d } d } d } xì t  d	  D]Þ }	 t j d
  t j j d | |	 t |  d |  |	 t |   | |	 t |  | |	 t |  | |	 t |  | |	 t |  | |	 t |  | |	 t |  d | |	 t |  d  t j j   qC Wd  S(   Nt   Lllllllt   oOooooot   aaAaaaat   dddDdddt   iiiiIiit   nnnnnNnt   ggggggGs   - _- _ i   gÉ?s   [0m[[1;36ms   [0m][1;31m s    [0m[[1;36ms   [0m](   t   ranget   timet   sleept   syst   stdoutt   writet   lent   flush(
   t   lt   ot   at   dt   it   nt   gt   st   pt   z(    (    s	   pentes.pyt   loading   s    ¾c           C   s   t  j d  d  S(   Nt   clear(   t   ost   system(    (    (    s	   pentes.pyR   '   s    c         C   sM   xF |  d D]: } t  j j |  t  j j   t j t j   d  q Wd  S(   Ns   
gü©ñÒMb ?(   R   R   R   R   R	   R
   t   random(   t   bR   (    (    s	   pentes.pyt   run*   s    c    
      C   s  t  d t d t  d t d GHt  d t d t  d t d GHt  d t d t  d t d GHt  d t d	 t  d t d
 GHt  d t d t  d t d GHt  d t d t  d t d GHt  d t d t  d t d GHt  d t d t  d t d GHt  d t d t  d t d GHt  d t d t  d t d GHt d t d t  d  }  |  d k s~|  d k rÎt   t d t d t  d  } t   t   t   t j d | d  n¿|  d k sæ|  d k r6t   t d t d t  d  } t   t   t   t j d | d  nW|  d k sN|  d k rt   t d t d t  d  } t   t   t   t j d | d  nï|  d  k s¶|  d	 k rt   t d t d t  d  } t   t   t   t j d! | d  n|  d" k s|  d k rkt   t d t d t  d  } t   t   t t j d | d  n"|  d# k s|  d k rÓt   t d t d t  d  } t   t   t   t j d$ | d  nº|  d% k së|  d k r;t   t d t d t  d  } t   t   t   t j d& | d  nR|  d' k sS|  d k r£t   t d t d t  d  } t   t   t   t j d( | d  nê |  d) k s»|  d k rt   t d t d t  d  }	 t   t   t   t j d* |	 d  n |  d+ k s#|  d k rZt   t d t	 d,  t
 j d-  t   t   n3 t d. t  |  GHt
 j d/  t   t   t   d  S(0   Nt   [t   01s   ] s
   DNS Lookupt   02s   GEO IP Lookupt   03s   http header checkt   04t   PINGt   05s	   Port Scant   06s   Reverse DNS Lookupt   07t
   Traceroutet   08s   Whois Lookupt   09s   Zone Tranfert   00t   Exitt    s   Choose: t   1s   Masukkan IP atau Domain: s.   curl http://api.hackertarget.com/dnslookup/?q=t   2s)   curl http://api.hackertarget.com/nmap/?q=t   3s1   curl https://api.hackertarget.com/httpheaders/?q=t   4s+   curl https://api.hackertarget.com/nping/?q=t   5t   6s0   curl https://api.hackertarget.com/reversedns/?q=t   7s)   curl https://api.hackertarget.com/mtr/?q=t   8s*   curl http://api.hackertarget.com/whois/?q=t   9s3   curl https://api.hackertarget.com/zonetransfer/?q=$t   0s   THANK FOR USING^_^i   s   tidak ada pilihan gÍÌÌÌÌÌô?(   R   t   ht   mt	   raw_inputR   R   R   R   R    t   cR	   R
   t   exitR    t   menu(
   R   t   dnst   geot   hhct   pingt   pst   rdlt   trct   wlt   zt(    (    s	   pentes.pyR?   2   sª    !!!!!!!!!!
(   R   R   R	   R   R;   R:   t   kR=   R   R    R   R   R    R?   (    (    (    s	   pentes.pyt   <module>   s   					X