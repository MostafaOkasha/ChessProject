'''1)Considering each square to be 2*2 units
2)predefined positions allocated for captured pieces and each square accomodates
two such capured pieces'''
import chess as c
import math
p1=r1=k1=b1=0
P=R=K=B=0
WhiteMove=None
BlackMove=None
motmov=False
l1={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
def movement():
    def WhiteInput():
        return raw_input("White : ")

    def BlackInput():
        return raw_input("Black : ")

    def isCapturing(WhiteMove):
        if board.piece_at(WhiteMove.to_square) == None:
            return False
        else:
            return True
    def pieceAt(SquareName):
        global l
        global board
        for i in range (len(l)):
            if l[i][0]==SquareName:
                return board.piece_at(l[i][1])
    def white():
        global BlackMove
        global motmov
        global f
        global t
        f=(str(WhiteMove))[:2]#position of the current piece
        t=(str(WhiteMove))[2:]#position to which the piece has to move
        s=str(pieceAt(f))#s contains the name of the piece at f(Eg:p,P,n....)
        s1=str(pieceAt(t))#s1 contains the name of the piece at t(Eg:p,P,n....)                  
        i=f[0]
        j=f[1]
        i1=t[0]
        j1=t[1]
        a=(str(BlackMove))[2:]
        b=(str(WhiteMove))[:2]
        N='N'
        S='S'
        W='W'
        E='E'
        NE='NE'
        SE='SE'
        SW='SW'
        NW='NW'
        A='A'
        D='D'
        AM='AM'
        DM='DM'
        def motor(a,b):#Movement of motor from black to white
            motmov=True                            
            a1=['a','b','c','d','e','f','g','h']
            n1=['1','2','3','4','5','6','7','8']
            l1={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
            l=[]
            if BlackMove!=None:#if its not the first move
                if isCapturing(WhiteMove)==False:
                    a=(str(BlackMove))[2:]
                    b=(str(WhiteMove))[:2]
                    for i in range(1,9):#storing all the diagonal elements in list
                        x=chr(ord(a[0])+i)
                        y=str(int(a[1])+i)
                        x1=chr(ord(a[0])-i)
                        y1=str(int(a[1])-i)
                        x2=chr(ord(a[0])-i)
                        y2=str(int(a[1])+i)
                        x3=chr(ord(a[0])+i)
                        y3=str(int(a[1])-i)
                        if x in a1 and y in n1:
                            l.append(x+y)
                        if x1 in a1 and y1 in n1:
                            l.append(x1+y1)
                        if x2 in a1 and y2 in n1:
                            l.append(x2+y2)
                        if x3 in a1 and y3 in n1:
                            l.append(x3+y3)
                    if a[0]==b[0] or a[1]==b[1]:#checking if it has to move straight
                        straight(a,b,motmov)
                    elif b in l:#checking if it moves diagonally
                        diagonal(a,b,motmov)
                    else:
                        if ord(a[0])<ord(b[0]) and int(a[1])<int(b[1]):#1st quad
                            n=(int(b[1])-int(a[1]))*2-1
                            e=(l1[b[0]]-l1[a[0]])*2-1
                            return([(AM),(E,1),(N,n),(E,e),(N,1),(DM)])
                        elif ord(a[0])>ord(b[0]) and int(a[1])<int(b[1]):#2nd quad
                            n=(int(b[1])-int(a[1]))*2-1
                            w=(l1[a[0]]-l1[b[0]])*2-1
                            return([(AM),(W,1),(N,n),(W,w),(N,1),(DM)])
                        elif ord(a[0])>ord(b[0]) and int(a[1])>int(b[1]):
                            s=(int(a[1])-int(b[1]))*2-1
                            w=(l1[a[0]]-l1[b[0]])*2-1
                            return([(AM),(W,1),(S,s),(W,w),(S,1),(DM)])
                        elif ord(a[0])<ord(b[0]) and int(a[1])>int(b[1]):
                            s=(int(a[1])-int(b[1]))*2-1
                            e=(l1[b[0]]-l1[a[0]])*2-1
                            return([(AM),(E,1),(S,s),(E,e),(S,1),(DM)])
                else:                   
                    a=(str(BlackMove))[2:]
                    b=(str(WhiteMove))[2:]
                    for i in range(1,9):
                        x=chr(ord(a[0])+i)
                        y=str(int(a[1])+i)
                        x1=chr(ord(a[0])-i)
                        y1=str(int(a[1])-i)
                        x2=chr(ord(a[0])-i)
                        y2=str(int(a[1])+i)
                        x3=chr(ord(a[0])+i)
                        y3=str(int(a[1])-i)
                        if x in a1 and y in n1:
                            l.append(x+y)
                        if x1 in a1 and y1 in n1:
                            l.append(x1+y1)
                        if x2 in a1 and y2 in n1:
                            l.append(x2+y2)
                        if x3 in a1 and y3 in n1:
                            l.append(x3+y3)
                    print('l',l)
                    if a[0]==b[0] or a[1]==b[1]:
                        straight(a,b,motmov)
                    elif b in l:
                        diagonal(a,b,motmov)
                    else:
                        if ord(a[0])<ord(b[0]) and int(a[1])<int(b[1]):
                            n=(int(b[1])-int(a[1]))*2-1
                            e=(l1[b[0]]-l1[a[0]])*2-1
                            return([(AM),(E,1),(N,n),(E,e),(N,1),(DM)])
                        elif ord(a[0])>ord(b[0]) and int(a[1])<int(b[1]):
                            n=(int(b[1])-int(a[1]))*2-1
                            w=(l1[a[0]]-l1[b[0]])*2-1                            
                            return([(AM),(W,1),(N,n),(W,w),(N,1),(DM)])
                        elif ord(a[0])>ord(b[0]) and int(a[1])>int(b[1]):
                            s=(int(a[1])-int(b[1]))*2-1
                            w=(l1[a[0]]-l1[b[0]])*2-1
                            return([(AM),(W,1),(S,s),(W,w),(S,1),(DM)])
                        elif ord(a[0])<ord(b[0]) and int(a[1])>int(b[1]):
                            s=(int(a[1])-int(b[1]))*2-1
                            e=(l1[b[0]]-l1[a[0]])*2-1
                            return([(AM),(E,1),(S,s),(E,e),(S,1),(DM)])
                    

        def straight(f,t,motmov):
            if f[0]==t[0]:
                vrr=(int(f[1])-int(t[1]))*2
                if vrr<0:
                    if motmov:
                        return([(AM),(N,abs(vrr)),(DM)])
                    else:
                        return([(A),(E,1),(N,abs(vrr)),(W,1),(D)])
                else:
                    if motmov:
                        return([(AM),(S,vrr),(DM)])
                    else:                                        
                        return([(A),(E,1),(S,vrr),(W,1),(D)])            
            else:
                hrr=(int(l1[f[0]])-int(l1[t[0]]))*2
                if hrr<0:
                    if motmov:
                        
                        return([(AM),(E,abs(hrr)),(DM)])
                    else:
                        if int(f[1])==1:
                            
                            return([(A),(N,1),(E,abs(hrr)),(S,1),(D)])
                        elif int(f[1])==8:
                            
                            return([(A),(S,1),(E,abs(hrr)),(N,1),(D)])
                        else:
                            
                            return([(A),(N,1),(E,abs(hrr)),(S,1),(D)])
                            
                            
                else:
                    if motmov:
                        
                        return([(AM),(W,hrr),(DM)])
                    else:
                        if int(f[1])==1:
                            
                            return([(A),(N,1),(W,hrr),(S,1),(D)])
                        elif int(f[1])==8:
                            
                            return([(A),(S,1),(E,abs(hrr)),(N,1),(D)])
                        else:
                            
                            return([(A),(N,1),(E,abs(hrr)),(S,1),(D)])
                            
                        
                        
        def diagonal(f,t,motmov):
            vbb=int(f[1])-int(t[1])
            hbb=l1[f[0]]-l1[t[0]]
            
            if vbb<0 and hbb<0:
                if motmov:
                    
                    return([(AM),(NE,vbb),(DM)])
                else:
                    
                    return([(A),(NE,vbb),(D)])         
            elif vbb<0 and hbb>0:
                if motmov:
                    
                    return([(AM),(NW,vbb),(DM)])
                else:
                    
                    return([(A),(NW,vbb),(D)])
            elif vbb>0 and hbb>0:
                if motmov:
                    
                    return([(AM),(SW,vbb),(DM)])
                else:
                    
                    return([(A),(SW,vbb),(D)])
            else:
                if motmov:
                    
                    return([(AM),(SE,vbb),(DM)])
                else:
                    
                    return([(A),(SE,vbb),(D)])

        def capBlack(s1):
            c=(str(BlackMove))[2:]
            d=(str(WhiteMove))[2:]
            motor(c,d)
            if s1=='p':
                global l
                global p1
                p1 = p1+1
                if p1==1 or p1==2:
                    v=(6-int(t[1]))*2
                elif p1==3 or p1==4:
                    v=(5-int(t[1]))*2
                elif p1==5 or p1==6:
                    v=(4-int(t[1]))*2
                else:
                    v=(3-int(t[1]))*2
                h=2*(l1[t[0]]-1)+1
                if v<0:
                    po=False
                else:
                    po=True        
                if p1==1 or p1==3 or p1==5 or p1==7:
                    h1=1.5
                    v1=0.5
                    b=True
                else:
                    h1=0.5
                    v2=0.5
                    b=False
                i2=int(((str(WhiteMove))[2:])[1])
                j2=int(((str(WhiteMove))[:2])[1])
                hm=abs((l1[((str(WhiteMove))[:2])[0]]*2)-1)
                vm=(abs(v/2)+i2-j2)*2
                
                if (i2-v/2)>j2:
                    mo=True
                else:
                    mo=False
                if po and b:
                    if mo:
                        if i2!=1:
                            
                            return([(A),(S,1),(W,h),(N,abs(v)),(W,h1),(N,v1),(D),(AM),(S,v1),(E,h1),(N,vm+2),(E,hm),(N,1),(DM)])
                        else:
                            
                            return([(A),(N,1),(W,h),(N,abs(v)-2),(W,h1),(N,v1),(D),(AM),(S,v1),(E,h1),(N,vm+2),(E,hm),(N,1),(DM)])
                    else:
                        if i2!=1:
                            
                            return([(A),(S,1),(W,h),(N,abs(v)),(W,h1),(N,v1),(D),(AM),(S,v1),(E,h1),(S,vm),(E,hm),(N,1),(DM)])
                        else:
                            
                            return([(A),(N,1),(W,h),(N,abs(v)-2),(W,h1),(N,v1),(D),(AM),(S,v1),(E,h1),(S,vm),(E,hm),(N,1),(DM)])                                         
                        
                elif po and not b:
                    if mo:
                        if i2!=1:
                            
                            return([(A),(S,1),(W,h),(N,abs(v)),(E,h1),(N,v2),(D),(AM),(S,v2),(E,h1),(N,vm+2),(E,hm),(N,1),(DM)])
                        else:
                            
                            return([(A),(N,1),(W,h),(N,abs(v)-2),(E,h1),(N,v2),(D),(AM),(S,v2),(E,h1),(N,vm+2),(E,hm),(N,1),(DM)])
                    else:
                        if i2!=1:
                            
                            return([(A),(S,1),(W,h),(N,abs(v)),(E,h1),(N,v2),(D),(AM),(S,v2),(E,h1),(S,vm),(E,hm),(N,1),(DM)])
                        else:
                            
                            return([(A),(N,1),(W,h),(N,abs(v)-2),(E,h1),(N,v2),(D),(AM),(S,v2),(E,h1),(S,vm),(E,hm),(N,1),(DM)])
                            
                elif not po and b:
                    if mo:
                        if i2!=1:
                            
                            return([(A),(S,1),(W,h),(S,abs(v)),(W,h1),(N,v1),(D),(AM),(S,v1),(E,h1),(N,vm+2),(E,hm),(S,1),(DM)])
                        else:
                            
                            return([(A),(N,1),(W,h),(S,abs(v)+2),(W,h1),(N,v1),(D),(AM),(S,v1),(E,h1),(N,vm+2),(E,hm),(S,1),(DM)])
                    else:
                        if i2!=1:
                            
                            return([(A),(S,1),(W,h),(S,abs(v)),(W,h1),(N,v1),(D),(AM),(S,v1),(E,h1),(S,vm),(E,hm),(N,1),(DM)])
                        else:
                            
                            return([(A),(N,1),(W,h),(S,abs(v)+2),(W,h1),(N,v1),(D),(AM),(S,v1),(E,h1),(S,vm),(E,hm),(N,1),(DM)])
                elif not po and not b:
                    if mo:
                        if i2!=1:
                            
                            return([(A),(S,1),(W,h),(S,abs(v)),(E,h1),(N,v2),(D),(AM),(S,v2),(E,h1),(N,vm+2),(E,hm),(S,1),(DM)])
                        else:
                            
                            return([(A),(N,1),(W,h),(S,abs(v)+2),(E,h1),(N,v2),(D),(AM),(S,v2),(E,h1),(N,vm+2),(E,hm),(S,1),(DM)])
                    else:
                        if i2!=1:
                            
                            return([(A),(S,1),(W,h),(S,abs(v)),(E,h1),(N,v2),(D),(AM),(S,v2),(E,h1),(S,vm),(E,hm),(N,1),(DM)])
                        else:
                            
                            return([(A),(N,1),(W,h),(S,abs(v)+2),(E,h1),(N,v2),(D),(AM),(S,v2),(E,h1),(S,vm),(E,hm),(N,1),(DM)])
                        
            elif s1=='n':
                global k1
                k1=k1+1
                hn=2*(l1[t[0]]-1)+1
                vn=(7-int(t[1]))*2
                if k1==1:
                    hn1=1.5
                    vn1=0.5
                    bn=True
                else:
                    hn1=0.5
                    vn2=0.5
                    bn=False
                i2=int(((str(WhiteMove))[2:])[1])
                j2=int(((str(WhiteMove))[:2])[1])
                hm=abs((l1[((str(WhiteMove))[:2])[0]]*2)-1)
                vm=(abs(vn/2)+i2-j2)*2
                if (i2-vn/2)>j2:
                    mo=True
                else:
                    mo=False
                if vn<0 and bn:
                    if mo:
                        if i2!=1:
                            
                            return([(A),(S,1),(W,hn),(S,abs(vn)),(W,hn1),(N,vn1),(D),(AM),(S,vn1),(E,hn1),(N,vm+2),(E,hm),(S,1),(DM)])
                        else:
                            
                            return([(A),(N,1),(W,hn),(S,abs(vn)+2),(W,hn1),(N,vn1),(D),(AM),(S,vn1),(E,hn1),(N,vm+2),(E,hm),(S,1),(DM)])
                            
                    else:
                         if i2!=1:
                            
                            return([(A),(S,1),(W,hn),(S,abs(vn)),(W,hn1),(N,vn1),(D),(AM),(N,vn1),(E,hn1),(S,vm),(E,hm),(N,1),(DM)])
                         else:
                            
                            return([(A),(N,1),(W,hn),(S,abs(vn)+2),(W,hn1),(N,vn1),(D),(AM),(N,vn1),(E,hn1),(S,vm),(E,hm),(N,1),(DM)])
                                                           
                elif vn<0 and not bn:
                    if mo:
                        if i2!=1:
                           
                           return([(A),(S,1),(W,hn),(S,abs(vn)),(W,hn1),(N,vn2),(D),(AM),(S,vn2),(E,hn1),(N,vm+2),(E,hm),(S,1),(DM)])
                        else:
                           
                            return([(A),(N,1),(W,hn),(S,abs(vn)+2),(W,hn1),(N,vn2),(D),(AM),(S,vn2),(E,hn1),(N,vm+2),(E,hm),(S,1),(DM)])
                    else:
                        if i2!=1:
                            
                            return([(A),(S,1),(W,hn),(S,abs(vn)),(W,hn1),(N,vn2),(D),(AM),(S,vn2),(E,hn1),(S,vm),(E,hm),(N,1),(DM)])
                        else:
                            
                            return([(A),(N,1),(W,hn),(S,abs(vn)+2),(W,hn1),(N,vn2),(D),(AM),(S,vn2),(E,hn1),(S,vm),(E,hm),(N,1),(DM)])
                        
                elif vn>0 and bn:
                    if mo:
                        if i2!=1:
                           
                           return([(A),(S,1),(W,hn),(N,abs(vn)),(W,hn1),(N,vn1),(D),(AM),(S,vn1),(E,hn1),(N,vm+2),(E,hm),(S,1),(DM)])
                        else:
                            
                            return([(A),(N,1),(W,hn),(N,abs(vn)-2),(W,hn1),(N,vn1),(D),(AM),(S,vn1),(E,hn1),(N,vm+2),(E,hm),(S,1),(DM)])
                            
                    else:
                        if i2!=1:
                            
                            return([(A),(S,1),(W,hn),(N,abs(vn)),(W,hn1),(N,vn1),(D),(AM),(S,vn1),(E,hn1),(S,vm),(E,hm),(N,1),(DM)])
                        else:
                           
                            return([(A),(N,1),(W,hn),(N,abs(vn)-2),(W,hn1),(N,vn1),(D),(AM),(S,vn1),(E,hn1),(S,vm),(E,hm),(N,1),(DM)])
                        
                else:
                    if mo:
                        if i2!=1:
                           
                           return([(A),(S,1),(W,hn),(N,abs(vn)),(W,hn1),(N,vn2),(D),(AM),(S,vn2),(E,hn1),(N,vm+2),(E,hm),(S,1),(DM)])
                        else:
                           
                           return([(A),(N,1),(W,hn),(N,abs(vn)-2),(W,hn1),(N,vn2),(D),(AM),(S,vn2),(E,hn1),(N,vm+2),(E,hm),(S,1),(DM)])
                            
                    else:
                        if i2!=1:
                            
                            return([(A),(S,1),(W,hn),(N,abs(vn)),(W,hn1),(N,vn2),(D),(AM),(S,vn2),(E,hn1),(S,vm),(E,hm),(N,1),(DM)])
                        else:
                            
                            return([(A),(N,1),(W,hn),(N,abs(vn)-2),(W,hn1),(N,vn2),(D),(AM),(S,vn2),(E,hn1),(S,vm),(E,hm),(N,1),(DM)])                                        
                        
                           
            elif s1=='r':
                global r1
                r1=r1+1
                hr=2*(l1[t[0]]-1)+1
                vr=(8-int(t[1]))*2
                if r1==1:
                    hr1=1.5
                    vr1=0.5
                    br=True
                else:
                    hr1=0.5
                    vr2=0.5
                    br=False
                i2=int(((str(WhiteMove))[2:])[1])
                j2=int(((str(WhiteMove))[:2])[1])
                hm=abs((l1[((str(WhiteMove))[:2])[0]]*2)-1)
                vm=(abs(vr/2)+i2-j2)*2
                if i2-vr/2>j2:
                    mo=True
                else:
                    mo=False
                if vr<0 and br:
                    if not mo:
                        if i2!=1:
                           
                            return([(A),(S,1),(W,hr),(S,abs(vr)),(W,hr1),(N,vr1),(D),(AM),(S,vr1),(E,hr1),(S,vm),(E,hm),(N,1),(DM)])
                        else:
                            
                            return([(A),(N,1),(W,hr),(S,abs(vr)+2),(W,hr1),(N,vr1),(D),(AM),(S,vr1),(E,hr1),(S,vm),(E,hm),(N,1),(DM)])
                            
                    else:
                        if i2!=1:
                            
                            return([(A),(S,1),(W,hr),(S,abs(vr)),(W,hr1),(N,vr1),(D),(AM),(S,vr1),(E,hr1),(N,vm+2),(E,hm),(S,1),(DM)])
                        else:
                            
                            return([(A),(N,1),(W,hr),(S,abs(vr)+2),(W,hr1),(N,vr1),(D),(AM),(S,vr1),(E,hr1),(N,vm+2),(E,hm),(S,1),(DM)])
                elif vr<0 and not br:
                    if not mo:
                        if i2!=1:
                            
                            return([(A),(S,1),(W,hr),(S,abs(vr)),(W,hr1),(N,vr2),(D),(AM),(S,vr2),(E,hr1),(S,vm),(E,hm),(N,1),(DM)])
                        else:
                            
                            return([(A),(N,1),(W,hr),(S,abs(vr)+2),(W,hr1),(N,vr2),(D),(AM),(S,vr2),(E,hr1),(S,vm),(E,hm),(N,1),(DM)])
                    else:
                        if i2!=1:
                            
                            return([(A),(S,1),(W,hr),(S,abs(vr)),(W,hr1),(N,vr2),(D),(AM),(S,vr2),(E,hr1),(N,vm+2),(E,hm),(S,1),(DM)])
                        else:
                            
                            return([(A),(N,1),(W,hr),(S,abs(vr)+2),(W,hr1),(N,vr2),(D),(AM),(S,vr2),(E,hr1),(N,vm+2),(E,hm),(S,1),(DM)])
                            
                elif vr>0 and br:
                    if not mo:
                        if i2!=1:
                            
                            return([(A),(S,1),(W,hr),(N,abs(vr)),(W,hr1),(N,vr1),(D),(AM),(S,vr1),(E,hr1),(S,vm),(E,hm),(N,1),(DM)])
                        else:
                            
                            return([(A),(N,1),(W,hr),(N,abs(vr)+2),(W,hr1),(N,vr1),(D),(AM),(S,vr1),(E,hr1),(S,vm),(E,hm),(N,1),(DM)])
                            
                    else:
                        if i2!=1:
                            
                            return([(A),(S,1),(W,hr),(N,abs(vr)),(W,hr1),(N,vr1),(D),(AM),(S,vr1),(E,hr1),(N,vm+2),(E,hm),(S,1),(DM)])
                        else:
                            
                            return([(A),(N,1),(W,hr),(N,abs(vr)+2),(W,hr1),(N,vr1),(D),(AM),(S,vr1),(E,hr1),(N,vm+2),(E,hm),(S,1),(DM)])
                            
                else:
                    if not mo:
                        if i2!=1:
                            
                            return([(A),(S,1),(W,hr),(N,abs(vr)),(W,hr1),(N,vr2),(D),(AM),(S,vr2),(E,hr1),(S,vm),(E,hm),(N,1),(DM)])
                        else:
                            
                            return([(A),(N,1),(W,hr),(N,abs(vr)+2),(W,hr1),(N,vr2),(D),(AM),(S,vr2),(E,hr1),(S,vm),(E,hm),(N,1),(DM)])                                            
                    else:
                        if i2!=1:
                            
                            return([(A),(S,1),(W,hr),(N,abs(vr)),(W,hr1),(N,vr2),(D),(AM),(S,vr2),(E,hr1),(N,vm+2),(E,hm),(S,1),(DM)])
                        else:
                            
                            return([(A),(N,1),(W,hr),(N,abs(vr)+2),(W,hr1),(N,vr2),(D),(AM),(S,vr2),(E,hr1),(N,vm+2),(E,hm),(S,1),(DM)])
                            
                               
            elif s1=='b':
                global b1
                b1=b1+1
                hb=2*(l1[t[0]]-1)+1
                vb=(2-int(t[1]))*2
                if b==1:
                    hb1=1.5
                    vb1=0.5
                    bb=True
                else:
                    vb1=1
                    hb1=0.5
                    vb2=0.5
                    bb=False
                i2=int(((str(WhiteMove))[2:])[1])
                j2=int(((str(WhiteMove))[:2])[1])
                hm=(l1[((str(WhiteMove))[:2])[0]]*2)-1
                vm=(abs(vb/2)+i2-j2)*2
                if i2-(vb/2)>j2:
                    mo=True
                else:
                    mo=False
                if vb<0 and bb:
                    if mo:
                        if i2!=1:
                            
                            return([(A),(S,1),(W,hb),(S,abs(vb)),(W,hb1),(N,vb1),(D),(AM),(S,vb1),(E,hb1),(N,vm+2),(E,hm),(S,1),(DM)])
                        else:
                            
                            return([(A),(N,1),(W,hb),(S,abs(vb)+2),(W,hb1),(N,vb1),(D),(AM),(S,vb1),(E,hb1),(N,vm+2),(E,hm),(S,1),(DM)])
                            
                    else:
                        if i2!=1:
                            
                            return([(A),(S,1),(W,hb),(S,abs(vb)),(W,hb1),(N,vb1),(D),(AM),(S,vb1),(E,hb1),(S,vm),(E,hm),(N,1),(DM)])
                        else:
                            
                            return([(A),(N,1),(W,hb),(S,abs(vb)+2),(W,hb1),(N,vb1),(D),(AM),(S,vb1),(E,hb1),(S,vm),(E,hm),(N,1),(DM)])
                            
                elif vb<0 and not bb:
                    if mo:
                        if i2!=1:
                            
                            return([(A),(S,1),(W,hb),(S,abs(vb)+2),(W,hb1),(N,vb2),(D),(AM),(S,vb2),(E,hb1),(N,vm+2),(E,hm),(S,1),(DM)])
                        else:
                            
                            return([(A),(N,1),(W,hb),(S,abs(vb)+2),(W,hb1),(N,vb2),(D),(AM),(S,vb2),(E,hb1),(N,vm+2),(E,hm),(S,1),(DM)])

                            
                    else:
                        if i2!=1:
                            
                            return([(A),(S,1),(W,hb),(S,abs(vb)),(W,hb1),(N,vb2),(D),(AM),(S,vb2),(E,hb1),(S,vm),(E,hm),(N,1),(DM)])
                        else:
                            
                            return([(A),(N,1),(W,hb),(S,abs(vb)+2),(W,hb1),(N,vb2),(D),(AM),(S,vb2),(E,hb1),(S,vm),(E,hm),(N,1),(DM)])
                            
                        
                elif vb>0 and bb:
                    if mo:
                        if i2!=1:
                           
                            return([(A),(S,1),(W,hb),(N,abs(vb)),(W,hb1),(N,vb1),(D),(AM),(S,vb1),(E,hb1),(N,vm+2),(E,hm),(S,1),(DM)])
                        else:
                            
                            return([(A),(N,1),(W,hb),(N,abs(vb)+2),(W,hb1),(N,vb1),(D),(AM),(S,vb1),(E,hb1),(N,vm+2),(E,hm),(S,1),(DM)])
                            
                    else:
                        if i2!=1:
                            
                            return([(A),(S,1),(W,hb),(N,abs(vb)),(W,hb1),(N,vb1),(D),(AM),(S,vb1),(E,hb1),(S,vm),(E,hm),(N,1),(DM)])
                        else:
                            
                            return([(A),(N,1),(W,hb),(N,abs(vb)+2),(W,hb1),(N,vb1),(D),(AM),(S,vb1),(E,hb1),(S,vm),(E,hm),(N,1),(DM)])
                            
                else:
                    if mo:
                        if i2!=1:
                            
                            return([(A),(S,1),(W,hb),(N,abs(vb)),(W,hb1),(N,vb2),(D),(AM),(S,vb2),(E,hb1),(N,vm+2),(E,hm),(S,1),(DM)])
                        else:
                            
                            return([(A),(N,1),(W,hb),(N,abs(vb)+2),(W,hb1),(N,vb2),(D),(AM),(S,vb2),(E,hb1),(N,vm+2),(E,hm),(S,1),(DM)])                                            
                    else:
                        if i2!=1:
                            
                            return([(A),(S,1),(W,hb),(N,abs(vb)),(W,hb1),(N,vb2),(D),(AM),(S,vb2),(E,hb1),(S,vm),(E,hm),(N,1),(DM)])
                        else:
                            
                            return([(A),(N,1),(W,hb),(N,abs(vb)+2),(W,hb1),(N,vb2),(D),(AM),(S,vb2),(E,hb1),(S,vm),(E,hm),(N,1),(DM)])
                            
            elif s1=='q':
                hq=2*(l1[t[0]]-1)+1
                vq=(int(t[1])-1)*2
                hb1=0.5
                vb2=0.5
                i2=int(((str(WhiteMove))[2:])[1])
                j2=int(((str(WhiteMove))[:2])[1])
                hm=(l1[((str(WhiteMove))[:2])[0]]*2)-1
                vm=(abs(vq/2)+i2-j2)*2
                if i2-(vq/2)>j2:
                    if i2!=1:
                            
                            return([(A),(S,1),(W,hq),(S,vq),(W,hq1),(N,vq2),(D),(AM),(S,vq2),(E,hq1),(N,vm+2),(E,hm),(S,1),(DM)])
                    else:
                            
                            return([(A),(N,1),(W,hq),(S,vq+2),(W,hq1),(N,vq2),(D),(AM),(S,vq2),(E,hq1),(N,vm+2),(E,hm),(S,1),(DM)])                                    
                else:
                    if i2!=1:
                         
                         return([(A),(S,1),(W,hq),(S,vq),(W,hq1),(N,vq2),(D),(AM),(S,vq2),(E,hq1),(S,vm),(E,hm),(N,1),(DM)])
                    else:
                         
                         return([(A),(N,1),(W,hq),(S,vq+2),(W,hq1),(N,vq2),(D),(AM),(S,vq2),(E,hq1),(S,vm),(E,hm),(N,1),(DM)])
                        
                    
                    
                
            
            
        def Pawn():
            if isCapturing(WhiteMove):#checks if its an attacking move or not
                capBlack(s1)#calls the function that enables the movement of captured pieces
                if t==chr(ord(i)+1)+str(int(j)+1):#diagonal movement in NE
                    
                    return([(A),(NE,1),(D)])
                else:
                    
                    return([(A),(NW,1),(D)])#diagonal movement in NW
            else:
                if t==i+str(int(j)+1):#Checks if the move is 1 step or 2 steps
                    
                    return([(A),(N,2),(D)])
                else:
                    
                    return([(A),(N,4),(D)])
        def Rook():
            if isCapturing(WhiteMove):
                #motor((str(BlackMove))[:2],(str(BlackMove))[2:])
                capBlack(s1)
                straight(f,t,False)
            else:
                straight(f,t,False)
        
        def Bishop():
            if isCapturing(WhiteMove):
                #motor((str(BlackMove))[:2],(str(BlackMove))[2:])
                capBlack(s1)
                diagonal(f,t,False)
            else:
                diagonal(f,t,False)
        def Queen():
            if isCapturing(WhiteMove):
                #motor((str(BlackMove))[:2],(str(BlackMove))[2:])
                capBlack(s1)
                if f[0]==t[0] or f[1]==t[1]:#checks if the movement has to be horizontal/vertical or diagonal
                    straight(f,t,False)
                else:
                    diagonal(f,t,False)
            else:
                if f[0]==t[0] or f[1]==t[1]:
                    straight(f,t,False)
                else:
                    diagonal(f,t,False)
        def King():
            if isCapturing(WhiteMove):
                #motor((str(BlackMove))[:2],(str(BlackMove))[2:])
                capBlack(s1)
                if f[0]==t[0] or f[1]==t[1]:
                    straight(f,t,False)
                else:
                    diagonal(f,t,False)
            else:
                if f[0]==t[0] or f[1]==t[1]:
                    straight(f,t,False)
                else:
                    diagonal(f,t,False)
        def Knight():
            i=f[0]
            j=f[1]
            if isCapturing(WhiteMove):
                #motor((str(BlackMove))[:2],(str(BlackMove))[2:])
                capBlack(s1)
                if t==chr(ord(i)-2)+str(int(j)-1):
                          
                          return([(A),(S,1),(W,4),(S,1),(D)])
                elif t==chr(ord(i)-2)+str(int(j)+1):
                            
                            return([(A),(N,1),(W,4),(N,1),(D)])
                elif t==chr(ord(i)-1)+str(int(j)-2):
                           
                            return([(A),(W,1),(S,4),(E,1),(D)])
                elif t==chr(ord(i)+1)+str(int(j)-2):
                           
                            return([(A),(E,1),(S,4),(E,1),(D)])
                elif t==chr(ord(i)+2)+str(int(j)-1):
                            
                            return([(A),(S,1),(E,4),(S,1),(D)])
                elif t==chr(ord(i)+2)+str(int(j)+1):
                           
                            return([(A),(N,1),(E,4),(N,1),(D)])
                elif t==chr(ord(i)-1)+str(int(j)+2):
                           
                            return([(A),(W,1),(N,4),(W,1),(D)])
                else:
                           
                            return([(A),(E,1),(N,4),(E,1),(D)])
            else:
                if t==chr(ord(i)-2)+str(int(j)-1):
                            
                            return([(A),(S,1),(W,4),(S,1),(D)])
                elif t==chr(ord(i)-2)+str(int(j)+1):
                            
                            return([(A),(N,1),(W,4),(N,1),(D)])
                elif t==chr(ord(i)-1)+str(int(j)-2):
                           
                            return([(A),(W,1),(S,4),(E,1),(D)])
                elif t==chr(ord(i)+1)+str(int(j)-2):
                            
                            return([(A),(E,1),(S,4),(E,1),(D)])
                elif t==chr(ord(i)+2)+str(int(j)-1):
                            
                            return([(A),(S,1),(E,4),(S,1),(D)])
                elif t==chr(ord(i)+2)+str(int(j)+1):
                            
                            return([(A),(N,1),(E,4),(N,1),(D)])
                elif t==chr(ord(i)-1)+str(int(j)+2):
                          
                            return([(A),(W,1),(N,4),(W,1),(D)])
                else:
                            
                            return([(A),(E,1),(N,4),(E,1),(D)])
            

        
        def check(z):
            if z=='P':
                Pawn()
            elif z=='R':
                Rook()
            elif z=='N':
                Knight()
            elif z=='B':
                Bishop()
            elif z=='Q':
                Queen()
            elif z=='K':
                King()
            
        if isCapturing(WhiteMove)==False:
           
            motor(a,b)
        check(s)
    def Black():
        f=str(BlackMove)[:2]#position of the current piece
        t=str(BlackMove)[2:]#position to which the piece has to move
        s=str(pieceAt(f))#s contains the name of the piece at f(Eg:p,P,n....)
        s1=str(pieceAt(t))#s1 contains the name of the piece at t(Eg:p,P,n....)
        i=f[0]
        j=f[1]
        i1=t[0]
        j1=t[1]
        a=(str(WhiteMove))[2:]
        b=(str(BlackMove))[:2]
        N='N'
        S='S'
        W='W'
        E='E'
        NE='NE'
        SE='SE'
        SW='SW'
        NW='NW'
        AM='AM'
        DM='DM'
        A='A'
        D='D'
        def motor(a,b):#Movement of motor from white to black
                motmov=True                            
                a1=['a','b','c','d','e','f','g','h']
                n1=['1','2','3','4','5','6','7','8']
                l1={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
                l=[]
                if isCapturing(BlackMove)==False:
                    a=(str(WhiteMove))[2:]
                    b=(str(BlackMove))[:2]
                    for i in range(1,9):
                        x=chr(ord(a[0])+i)
                        y=str(int(a[1])+i)
                        x1=chr(ord(a[0])-i)
                        y1=str(int(a[1])-i)
                        x2=chr(ord(a[0])-i)
                        y2=str(int(a[1])+i)
                        x3=chr(ord(a[0])+i)
                        y3=str(int(a[1])-i)
                        if x in a1 and y in n1:
                            l.append(x+y)
                        if x1 in a1 and y1 in n1:
                            l.append(x1+y1)
                        if x2 in a1 and y2 in n1:
                            l.append(x2+y2)
                        if x3 in a1 and y3 in n1:
                            l.append(x3+y3)
                    if a[0]==b[0] or a[1]==b[1]:
                            straight(a,b,motmov)
                    elif b in l:
                            diagonal(a,b,motmov)
                    else:
                            if ord(a[0])<ord(b[0]) and int(a[1])<int(b[1]):
                                n=(int(b[1])-int(a[1]))*2-1
                                e=(l1[b[0]]-l1[a[0]])*2-1
                                return([(AM),(E,1),(N,n),(E,e),(N,1),(DM)])
                            elif ord(a[0])>ord(b[0]) and int(a[1])<int(b[1]):
                                n=(int(b[1])-int(a[1]))*2-1
                                w=(l1[b[0]]-l1[a[0]])*2-1
                                return([(AM),(W,1),(N,n),(W,w),(N,1),(DM)])
                            elif ord(a[0])>ord(b[0]) and int(a[1])>int(b[1]):
                                s=(int(a[1])-int(b[1]))*2-1
                                w=(l1[a[0]]-l1[b[0]])*2-1
                                return([(AM),(W,1),(S,s),(W,w),(S,1),(DM)])
                            elif ord(a[0])<ord(b[0]) and int(a[1])>int(b[1]):
                                s=(int(a[1])-int(b[1]))*2-1
                                e=(l1[b[0]]-l1[a[0]])*2-1
                                return([(AM),(E,1),(S,s),(E,e),(S,1),(DM)])
                else:
                        a=(str(WhiteMove))[2:]
                        b=(str(BlackMove))[2:]
                        for i in range(1,9):
                            x=chr(ord(a[0])+i)
                            y=str(int(a[1])+i)
                            x1=chr(ord(a[0])-i)
                            y1=str(int(a[1])-i)
                            x2=chr(ord(a[0])-i)
                            y2=str(int(a[1])+i)
                            x3=chr(ord(a[0])+i)
                            y3=str(int(a[1])-i)
                            if x in a1 and y in n1:
                                l.append(x+y)
                            if x1 in a1 and y1 in n1:
                                l.append(x1+y1)
                            if x2 in a1 and y2 in n1:
                                l.append(x2+y2)
                            if x3 in a1 and y3 in n1:
                                l.append(x3+y3)
                        if a[0]==b[0] or a[1]==b[1]:
                            straight(a,b,motmov)
                        elif b in l:
                            diagonal(a,b,motmov)
                        else:
                            if ord(a[0])<ord(b[0]) and int(a[1])<int(b[1]):
                                n=(int(b[1])-int(a[1]))*2-1
                                e=(l1[b[0]]-l1[a[0]])*2-1
                                return([(AM),(E,1),(N,n),(E,e),(N,1),(DM)])
                            elif ord(a[0])>ord(b[0]) and int(a[1])<int(b[1]):
                                n=(int(b[1])-int(a[1]))*2-1
                                w=(l1[a[0]]-l1[b[0]])*2-1
                                return([(AM),(W,1),(N,n),(W,w),(N,1),(DM)])
                            elif ord(a[0])>ord(b[0]) and int(a[1])>int(b[1]):
                                s=(int(a[1])-int(b[1]))*2-1
                                w=(l1[a[0]]-l1[b[0]])*2-1
                                return([(AM),(W,1),(S,s),(W,w),(S,1),(DM)])
                            elif ord(a[0])<ord(b[0]) and int(a[1])>int(b[1]):
                                s=(int(a[1])-int(b[1]))*2-1
                                e=(l1[b[0]]-l1[a[0]])*2-1
                                return([(AM),(E,1),(S,s),(E,e),(S,1),(DM)])
            
        def straight(f,t,motmov):
            if f[0]==t[0]:
                    vrr=(int(f[1])-int(t[1]))*2
                    if vrr<0:
                        if  motmov:
                                return([(AM),(N,abs(vrr)),(DM)])
                        else:
                            return([(A),(E,1),(N,abs(vrr)),(W,1),(D)])
                    else:
                        if motmov:
                                return([(AM),(S,vrr),(DM)])
                        else:
                            return([(AM),(E,1),(S,vrr),(W,1),(DM)])
            else:
                hrr=(int(l1[f[0]])-int(l1[t[0]]))*2
                if hrr<0:
                    if motmov:
                               return([(AM),(E,abs(hrr)),(DM)])
                    else:
                        if f[1]!=1:
                            return([(A),(S,1),(E,abs(hrr)),(N,1),(D)])
                        else:
                            return([(A),(N,1),(E,abs(hrr)),(S,1),(D)])
                else:
                    if motmov:
                               return([(AM),(W,hrr),(DM)])
                    else:
                        if f[1]!=1:
                               return([(A),(S,1),(W,hrr),(N,1),(D)])
                        else:
                            return([(A),(N,1),(W,hrr),(S,1),(D)])
                    
                        

        def diagonal(f,t,motmov):
            vbb=int(f[1])-int(t[1])
            hbb=l1[f[0]]-l1[t[0]]
            if vbb<0 and hbb<0:
                if motmov:
                               return([(AM),(NE,vbb),(DM)])
                else:
                                return([(A),(NE,vbb),(D)])
            elif vbb<0 and hbb>0:
                if motmov:
                                
                                return([(AM),(NW,vbb),(DM)])
                else:
                                
                                return([(A),(NW,vbb),(D)])
            elif vbb>0 and hbb>0:
                if motmov:
                                
                                return([(AM),(SW,vbb),(DM)])
                else:
                                
                                return([(A),(SW,vbb),(D)])
            else:
                if motmov:
                                
                                return([(AM),(SE,vbb),(DM)])
                else:
                                
                                return([(A),(SE,vbb),(D)])
                    
        def capWhite(s1):
            c=(str(WhiteMove))[2:]
            d=(str(BlackMove))[2:]
            motor(c,d)
            if s1=='P':
                global l
                global P
                P=P+1
                if P==1 or P==2:
                    v=(3-int(t[1]))*2
                elif P==3 or P==4:
                    v=(4-int(t[1]))*2
                elif P==5 or P==6:
                    v=(5-int(t[1]))*2
                else:
                    v=(6-int(t[1]))*2
                h=2*(8-l1[t[0]])+1
                if v<0:#up
                    Po=False
                else:
                    Po=True        
                if P==1 or P==3 or P==5 or P==7:
                    h1=1.5
                    v1=0.5
                    b=True
                else:
                    h1=0.5
                    v2=0.5
                    b=False
                i2=int(((str(BlackMove))[2:])[1])
                j2=int(((str(BlackMove))[:2])[1])
                hm=abs(((8-(l1[(((str(BlackMove))[:2])[0])]))*2)+1)
                vm=abs((abs(v)+((j2-i2)*2)))
                if ((9-i2)-(v/2))>(9-j2):
                        mo=True
                else:
                        mo=False
                if Po and b:
                    if mo:
                        if i2!=1:
                            return([(A),(S,1),(E,h),(N,abs(v)),(E,h1),(N,v1),(D),(AM),(S,v1),(W,h1),(N,vm),(W,hm),(N,1),(DM)])
                        else:
                            return([(A),(N,1),(E,h),(N,abs(v)-2),(E,h1),(N,v1),(D),(AM),(S,v1),(W,h1),(N,vm),(W,hm),(N,1),(DM)])
                            
                    else:
                        if i2!=1:
                            return([(A),(S,1),(E,h),(N,abs(v)),(E,h1),(N,v1),(D),(AM),(S,v1),(W,h1),(S,vm+2),(W,hm),(S,1),(DM)])
                        else:
                            return([(A),(N,1),(E,h),(N,abs(v)-2),(E,h1),(N,v1),(D),(AM),(S,v1),(W,h1),(S,vm+2),(W,hm),(S,1),(DM)])
                            
                elif Po and not b:
                    if mo:
                        if i2!=1:
                            return([(A),(S,1),(E,h),(N,abs(v)),(E,h1),(N,v2),(D),(AM),(S,v2),(W,h1),(N,vm),(W,hm),(N,1),(DM)])
                        else:
                           return([(A),(N,1),(E,h),(N,abs(v)-2),(E,h1),(N,v2),(D),(AM),(S,v2),(W,h1),(N,vm),(W,hm),(N,1),(DM)])
                            
                    else:
                        if i2!=1:
                           return([(A),(S,1),(E,h),(N,abs(v)),(E,h1),(N,v2),(D),(AM),(S,v2),(W,h1),(S,vm+2),(W,hm),(S,1),(DM)])
                        else:
                           return([(A),(N,1),(E,h),(N,abs(v)-2),(E,h1),(N,v2),(D),(AM),(S,v2),(W,h1),(S,vm+2),(W,hm),(S,1),(DM)])
                elif not Po and b:
                    if mo:
                        if i2!=1:
                            return([(A),(S,1),(E,h),(S,abs(v)),(E,h1),(N,v1),(D),(AM),(S,v1),(W,h1),(N,vm),(W,hm),(N,1),(DM)])
                        else:
                            return([(A),(N,1),(E,h),(S,abs(v)+2),(E,h1),(N,v1),(D),(AM),(S,v1),(W,h1),(N,vm),(W,hm),(N,1),(DM)])
                            
                    else:
                        if i2!=1:
                            return([(A),(S,1),(E,h),(S,abs(v)),(E,h1),(N,v1),(D),(AM),(S,v1),(W,h1),(S,vm+2),(W,hm),(S,1),(DM)])
                        else:
                           return([(A),(N,1),(E,h),(S,abs(v)+2),(E,h1),(N,v1),(D),(AM),(S,v1),(W,h1),(S,vm+2),(W,hm),(S,1),(DM)])
                            
                elif not Po and not b:
                    if mo:
                        if i2!=1:
                            return([(A),(S,1),(E,h),(S,abs(v)),(E,h1),(N,v2),(D),(AM),(S,v1),(W,h1),(N,vm),(W,hm),(N,1),(DM)])
                        else:
                            return([(A),(N,1),(E,h),(S,abs(v)+2),(E,h1),(N,v2),(D),(AM),(S,v1),(W,h1),(N,vm),(W,hm),(N,1),(DM)])
                            
                    else:
                        if i2!=1:
                            return([(A),(S,1),(E,h),(S,abs(v)),(E,h1),(N,v2),(D),(AM),(S,v1),(W,h1),(S,vm+2),(W,hm),(S,1),(DM)])
                        else:
                            return([(A),(N,1),(E,h),(S,abs(v)+2),(E,h1),(N,v2),(D),(AM),(S,v1),(W,h1),(S,vm+2),(W,hm),(S,1),(DM)])
                            
                        
            elif s1=='N':
                global K
                K=K+1
                hn=2*(8-l1[t[0]])+1
                vn=(2-int(t[1]))*2
                if K==1:
                    hn1=1.5
                    vn1=0.5
                    bn=True
                else:
                    hn1=0.5
                    vn2=0.5
                    bn=False
                i2=int(((str(BlackMove))[2:])[1])
                j2=int(((str(BlackMove))[:2])[1])
                hm=abs(((8-(l1[(((str(BlackMove))[:2])[0])]))*2)+1)
                vm=abs(abs(vn)+(j2-i2)*2)
                if ((9-i2)-vn/2)>(9-j2):
                        mo=True
                else:
                        mo=False
                if vn<0 and bn:
                    if mo:
                        if i1!=1:
                            return([(A),(S,1),(E,hn),(S,abs(vn)),(E,hn1),(N,vn1),(D),(AM),(S,vn1),(W,hn1),(N,vm),(W,hm),(N,1),(DM)])
                        else:
                            return([(A),(N,1),(E,hn),(S,abs(vn)+2),(E,hn1),(N,vn1),(D),(AM),(S,vn1),(W,hn1),(N,vm),(W,hm),(N,1),(DM)])
                            
                    else:
                        if i1!=1:
                            return([(A),(S,1),(E,hn),(S,abs(vn)),(E,hn1),(N,vn1),(D),(AM),(S,vn1),(W,hn1),(S,vm+2),(W,hm),(S,1),(DM)])
                        else:
                            return([(A),(N,1),(E,hn),(S,abs(vn)+2),(E,hn1),(N,vn1),(D),(AM),(S,vn1),(W,hn1),(S,vm+2),(W,hm),(S,1),(DM)])
                            
                        
                elif vn<0 and not bn:
                    if mo:
                        if i2!=1:
                           return([(A),(S,1),(E,hn),(S,abs(vn)),(E,hn1),(N,vn2),(D),(AM),(S,vn2),(W,hn1),(N,vm),(W,hm),(N,1),(DM)])
                        else:
                           return([(A),(N,1),(E,hn),(S,abs(vn)+2),(E,hn1),(N,vn2),(D),(AM),(S,vn2),(W,hn1),(N,vm),(W,hm),(N,1),(DM)])
                            
                    else:
                        if i2!=1:
                           return([(A),(S,1),(E,hn),(S,abs(vn)),(E,hn1),(N,vn2),(D),(AM),(S,vn2),(W,hn1),(S,vm+2),(W,hm),(S,1),(DM)])
                        else:
                           return([(A),(N,1),(E,hn),(S,abs(vn)+2),(E,hn1),(N,vn2),(D),(AM),(S,vn2),(W,hn1),(S,vm+2),(W,hm),(S,1),(DM)])
                            
                elif vn>0 and bn:
                    if mo:
                        if i2!=1:
                           
                           return([(A),(S,1),(E,h),(N,abs(v)),(E,hn1),(N,vn1),(D),(AM),(S,vn1),(W,hn1),(N,vm),(W,hm),(N,1),(DM)])
                        else:
                           
                           return([(A),(N,1),(E,h),(N,abs(v)-2),(E,hn1),(N,vn1),(D),(AM),(S,vn1),(W,hn1),(N,vm),(W,hm),(N,1),(DM)])
                            
                    else:
                        if i2!=1:
                           
                           return([(A),(S,1),(E,h),(N,abs(v)),(E,hn1),(N,vn1),(D),(AM),(S,vn1),(W,hn1),(S,vm+2),(W,hm),(S,1),(DM)])
                        else:
                           
                           return([(A),(N,1),(E,h),(N,abs(v)-2),(E,hn1),(N,vn1),(D),(AM),(S,vn1),(W,hn1),(S,vm+2),(W,hm),(S,1),(DM)])
                        
                else:
                    if mo:
                        if i2!=1:
                           
                           return([(A),(S,1),(E,hn),(N,abs(vn)),(E,hn1),(N,vn2),(D),(AM),(S,vn1),(W,hn1),(N,vm),(W,hm),(N,1),(DM)])
                        else:
                           
                           return([(A),(N,1),(E,hn),(N,abs(vn)-2),(E,hn1),(N,vn2),(D),(AM),(S,vn1),(W,hn1),(N,vm),(W,hm),(N,1),(DM)])
                    else:
                        if i2!=1:
                          return([(A),(S,1),(E,hn),(N,abs(vn)),(E,hn1),(N,vn2),(D),(AM),(S,vn1),(W,hn1),(S,vm+2),(W,hm),(S,1),(DM)])
                        else:
                           return([(A),(N,1),(E,hn),(N,abs(vn)-2),(E,hn1),(N,vn2),(D),(AM),(S,vn1),(W,hn1),(S,vm+2),(W,hm),(S,1),(DM)])
                            
                               
            elif s1=='R':
                global R
                R=R+1
                hr=2*(8-l1[t[0]])+1
                vr=(2-int(t[1]))*2
                if R==1:
                    hr1=1.5
                    vr1=0.5
                    br=True
                else:
                    hr1=0.5
                    vr2=0.5
                    br=False
                i2=int(((str(BlackMove))[2:])[1])
                j2=int(((str(BlackMove))[:2])[1])
                hm=abs(((8-(l1[(((str(BlackMove))[:2])[0])]))*2)+1)
                vm=abs(abs(vr)+(j2-i2)*2)
                if ((9-i2)-vr/2)>(9-j2):
                        mo=True
                else:
                        mo=False
                if vr<0 and br:
                    if mo:
                        if i2!=0:
                            return([(A),(S,1),(E,hr),(S,abs(vr)),(E,hr1),(N,vr1),(D),(AM),(S,vr1),(W,hr1),(N,vm),(W,hm),(N,1),(DM)])
                        else:
                            return([(A),(N,1),(E,hr),(S,abs(vr)+2),(E,hr1),(N,vr1),(D),(AM),(S,vr1),(W,hr1),(N,vm),(W,hm),(N,1),(DM)])

                            
                    else:
                        if i2!=0:
                            return([(A),(S,1),(E,hr),(S,abs(vr)),(E,hr1),(N,vr1),(D),(AM),(S,vr1),(W,hr1),(S,vm+2),(W,hm),(S,1),(DM)])
                        else:
                            return([(A),(N,1),(E,hr),(S,abs(vr)+2),(E,hr1),(N,vr1),(D),(AM),(S,vr1),(W,hr1),(S,vm+2),(W,hm),(S,1),(DM)])
                            
                elif vr<0 and not br:
                    if mo:
                         if i2!=0:
                            return([(A),(S,1),(E,hr),(S,abs(vr)),(E,hr1),(N,vr2),(D),(AM),(S,vr2),(W,hr1),(N,vm),(W,hm),(N,1),(DM)])
                         else:
                             return([(A),(N,1),(E,hr),(S,abs(vr)+2),(E,hr1),(N,vr2),(D),(AM),(S,vr2),(W,hr1),(N,vm),(W,hm),(N,1),(DM)])
                            
                            
                    else:
                        if i2!=0:
                            return([(A),(S,1),(E,hr),(S,abs(vr)),(E,hr1),(N,vr2),(D),(AM),(S,vr2),(W,hr1),(S,vm+2),(W,hm),(S,1),(DM)])
                        else:
                            return([(A),(N,1),(E,hr),(S,abs(vr)+2),(E,hr1),(N,vr2),(D),(AM),(S,vr2),(W,hr1),(S,vm+2),(W,hm),(S,1),(DM)])
                            
                elif vr>0 and br:
                    if mo:
                        if i2!=0:
                            return([(A),(S,1),(E,hr),(N,abs(vr)),(E,hr1),(N,vr1),(D),(AM),(S,vr1),(W,hr1),(N,vm),(W,hm),(N,1),(DM)])
                        else:
                            return([(A),(N,1),(E,hr),(N,abs(vr)-2),(E,hr1),(N,vr1),(D),(AM),(S,vr1),(W,hr1),(N,vm),(W,hm),(N,1),(DM)])
                            
                    else:
                        if i2!=0:
                            return([(A),(S,1),(E,hr),(N,abs(vr)),(E,hr1),(N,vr1),(D),(AM),(S,vr1),(W,hr1),(S,vm+2),(W,hm),(S,1),(DM)])
                        else:
                            return([(A),(N,1),(E,hr),(N,abs(vr)-2),(E,hr1),(N,vr1),(D),(AM),(S,vr1),(W,hr1),(S,vm+2),(W,hm),(S,1),(DM)])
                        
                else:
                    if mo:
                        if i2!=0:
                            return([(A),(S,1),(E,hr),(N,abs(vr)),(E,hr1),(N,vr2),(D),(AM),(S,vr2),(W,hr1),(N,vm),(W,hm),(N,1),(DM)])
                        else:
                            return([(A),(N,1),(E,hr),(N,abs(vr)-2),(E,hr1),(N,vr2),(D),(AM),(S,vr2),(W,hr1),(N,vm),(W,hm),(N,1),(DM)])
                    else:
                        if i2!=0:
                            return([(A),(S,1),(E,hr),(N,abs(vr)),(E,hr1),(N,vr2),(D),(AM),(S,vr2),(W,hr1),(S,vm+2),(W,hm),(S,1),(DM)])
                        else:
                            return([(A),(N,1),(E,hr),(N,abs(vr)-2),(E,hr1),(N,vr2),(D),(AM),(S,vr2),(W,hr1),(S,vm+2),(W,hm),(S,1),(DM)])
                            
                        
            elif s1=='B':
                B=B+1
                hb=2*(8-l1[t[0]])+1
                vb=(7-int(t[1]))*2
                if B==1:
                    hb1=1.5
                    vb1=0.5
                    bb=True
                else:
                    vb1=1
                    hb1=0.5
                    vb2=0.5
                    bb=False
                i2=int(((str(BlackMove))[2:])[1])
                j2=int(((str(BlackMove))[:2])[1])
                hm=abs(((8-(l1[(((str(BlackMove))[:2])[0])]))*2)+1)
                vm=abs(abs(vb)+(j2-i2)*2)
                if ((9-i2)-vb/2)>(9-j2):
                        mo=True
                else:
                        mo=False
                if vb<0 and bb:
                    if mo:
                        if i2!=1:
                            return([(A),(S,1),(E,hb),(S,abs(vb)),(E,hb1),(N,vb1),(D),(AM),(S,vb1),(W,hb1),(N,vm),(W,hm),(N,1),(DM)])
                        else:
                            return([(A),(N,1),(E,hb),(S,abs(vb)+2),(E,hb1),(N,vb1),(D),(AM),(S,vb1),(W,hb1),(N,vm),(W,hm),(N,1),(DM)])
                            
                    else:
                        if i2!=1:
                            return([(A),(S,1),(E,hb),(S,abs(vb)),(E,hb1),(N,vb1),(D),(AM),(S,vb1),(W,hb1),(S,vm+2),(W,hm),(S,1),(DM)])
                        else:
                    
                            return([(A),(N,1),(E,hb),(S,abs(vb)+2),(E,hb1),(N,vb1),(D),(AM),(S,vb1),(W,hb1),(S,vm+2),(W,hm),(S,1),(DM)])
                            
                elif vb<0 and not bb:
                    if mo:
                        if i2!=1:
                            
                            return([(A),(S,1),(E,hb),(S,abs(vb)),(E,hb1),(N,vb2),(D),(AM),(S,vb2),(W,hb1),(N,vm),(W,hm),(N,1),(DM)])
                        else:
                            
                            return([(A),(N,1),(E,hb),(S,abs(vb)+2),(E,hb1),(N,vb2),(D),(AM),(S,vb2),(W,hb1),(N,vm),(W,hm),(N,1),(DM)])
                            
                            
                    else:
                        if i2!=1:
                            
                            return([(A),(S,1),(E,hb),(S,abs(vb)),(E,hb1),(N,vb2),(D),(AM),(S,vb2),(W,hb1),(S,vm+2),(W,hm),(S,1),(DM)])
                        else:
                            
                            return([(A),(N,1),(E,hb),(S,abs(vb)+2),(E,hb1),(N,vb2),(D),(AM),(S,vb2),(W,hb1),(S,vm+2),(W,hm),(S,1),(DM)])                                       
                        
                elif vb>0 and bb:
                    if mo:
                        if i2!=1:
                            
                            return([(A),(S,1),(E,hb),(N,abs(vb)),(E,hb1),(N,vb1),(D),(AM),(S,vb1),(W,hb1),(N,vm),(W,hm),(N,1),(DM)])
                        else:
                            
                            return([(A),(N,1),(E,hb),(N,abs(vb)-2),(E,hb1),(N,vb1),(D),(AM),(S,vb1),(W,hb1),(N,vm),(W,hm),(N,1),(DM)])
                            
                    else:
                        if i2!=1:
                            
                            return([(A),(S,1),(E,hb),(N,abs(vb)),(E,hb1),(N,vb1),(D),(AM),(S,vb1),(W,hb1),(S,vm+2),(W,hm),(S,1),(DM)])
                        else:
                            
                            return([(A),(N,1),(E,hb),(N,abs(vb)-2),(E,hb1),(N,vb1),(D),(AM),(S,vb1),(W,hb1),(S,vm+2),(W,hm),(S,1),(DM)])
                            
                else:
                    if mo:
                        if i2!=1:
                           
                            return([(A),(S,1),(E,hb),(N,abs(vb)),(E,hb1),(N,vb2),(D),(AM),(S,vb2),(W,hb1),(N,vm),(W,hm),(N,1),(DM)])
                        else:
                            
                            return([(A),(N,1),(E,hb),(N,abs(vb)-2),(E,hb1),(N,vb2),(D),(AM),(S,vb2),(W,hb1),(N,vm),(W,hm),(N,1),(DM)])
                    else:
                        if i2!=1:
                            
                            return([(A),(S,1),(E,hb),(N,abs(vb)),(E,hb1),(N,vb2),(D),(AM),(S,vb2),(W,hb1),(S,vm+2),(W,hm),(S,1),(DM)])
                        else:
                            
                            return([(A),(N,1),(E,hb),(N,abs(vb)-2),(E,hb1),(N,vb2),(D),(AM),(S,vb2),(W,hb1),(S,vm+2),(W,hm),(S,1),(DM)])
                            
                        
            elif s1=='Q':
                hq=2*(8-l1[t[0]])+1
                vq=(8-int(t[1]))*2
                hb1=0.5
                vb2=0.5
                i2=int(((str(BlackMove))[2:])[1])
                j2=int(((str(BlackMove))[:2])[1])
                hm=abs(((8-(l1[(((str(BlackMove))[:2])[0])]))*2)+1)
                vm=abs(vq+(j2-i2)*2)
                if ((9-i2)-vq/2)>(9-j2):
                        mo=True
                else:
                        mo=False
                if mo:
                    if i2!=1:
                        return([(A),(S,1),(W,hq),(S,vq),(W,hq1),(N,vq2),(D),(AM),(S,vb2),(W,hb1),(N,vm),(W,hm),(N,1),(DM)])
                    else:
                        return([(A),(N,1),(W,hq),(S,vq+2),(W,hq1),(N,vq2),(D),(AM),(S,vb2),(W,hb1),(N,vm),(W,hm),(N,1),(DM)])
                        
                else:
                    if i2!=1:
                        return([(A),(S,1),(W,hq),(S,vq),(W,hq1),(N,vq2),(D),(AM),(S,vb2),(W,hb1),(S,vm+2),(W,hm),(S,1),(DM)])
                    else:
                        return([(A),(N,1),(W,hq),(S,vq+2),(W,hq1),(N,vq2),(D),(AM),(S,vb2),(W,hb1),(S,vm+2),(W,hm),(S,1),(DM)])
                        
        def pawn(s1):
            if isCapturing(BlackMove):
                    capWhite(s1)
                    if t==chr(ord(i)+1)+str(int(j)-1):
                        
                        return([(A),(SE,1),(D)])
                    else:
                        
                        return([(A),(SW,1),(D)])
            else:
                if t==i+str(int(j)-1):
                    
                    return([(A),(S,2),(D)])
                else:
                    
                    return([(A),(S,4),(D)])
        def Rook(s1):
            if isCapturing(BlackMove):
                    capWhite(s1)
                    straight(f,t,False)
            else:
                straight(f,t,False)
                
        def Bishop(s1):
            if isCapturing(BlackMove):
                    capWhite(s1)
                    diagonal(f,t,False)
            else:
                diagonal(f,t,False)
        def Queen(s1):
            if isCapturing(BlackMove):
                    capWhite(s1)
                    if f[0]==t[0] or f[1]==t[1]:
                        straight(f,t,False)
                    else:
                        diagonal(f,t,False)
            else:
                if f[0]==t[0] or f[1]==t[1]:
                    straight(f,t,False)
                else:
                    diagonal(f,t,False)
        def King(s1):
            if isCapturing(BlackMove):
                    capWhite(s1)
                    if f[0]==t[0] or f[1]==t[1]:
                        straight(f,t,False)
                    else:
                        diagonal(f,t,False)
            else:
                if f[0]==t[0] or f[1]==t[1]:
                    straight(f,t,False)
                else:
                    diagonal(f,t,False)
        def Knight(s1):
            i=f[0]
            j=f[1]
            if isCapturing(BlackMove):
                    capWhite(s1)
                    if t==chr(ord(i)-2)+str(int(j)-1):
                              
                              return([(A),(S,1),(W,4),(S,1),(D)])
                    elif t==chr(ord(i)-2)+str(int(j)+1):
                               
                                return([(A),(N,1),(W,4),(N,1),(D)])
                    elif t==chr(ord(i)-1)+str(int(j)-2):
                                return([(A),(W,1),(S,4),(W,1),(D)])
                    elif t==chr(ord(i)+1)+str(int(j)-2):
                               
                                return([(A),(E,1),(S,4),(E,1),(D)])
                    elif t==chr(ord(i)+2)+str(int(j)-1):
                                
                                return([(A),(S,1),(E,4),(S,1),(D)])
                    elif t==chr(ord(i)+2)+str(int(j)+1):
                                
                                return([(A),(N,1),(E,4),(N,1),(D)])
                    elif t==chr(ord(i)-1)+str(int(j)+2):
                                
                                return([(A),(W,1),(N,4),(W,1),(D)])
                    else:
                                
                                return([(A),(E,1),(N,4),(E,1),(D)])
            else:
                    if t==chr(ord(i)-2)+str(int(j)-1):
                              
                              return([(A),(S,1),(W,4),(S,1),(D)])
                    elif t==chr(ord(i)-2)+str(int(j)+1):
                                
                                return([(A),(N,1),(W,4),(N,1),(D)])
                    elif t==chr(ord(i)-1)+str(int(j)-2):
                                
                                return([(A),(W,1),(S,4),(W,1),(D)])
                    elif t==chr(ord(i)+1)+str(int(j)-2):
                                
                                return([(A),(E,1),(S,4),(E,1),(D)])
                    elif t==chr(ord(i)+2)+str(int(j)-1):
                               
                                return([(A),(S,1),(E,4),(S,1),(D)])
                    elif t==chr(ord(i)+2)+str(int(j)+1):
                                
                                return([(A),(N,1),(E,4),(N,1),(D)])
                    elif t==chr(ord(i)-1)+str(int(j)+2):
                               
                                return([(A),(W,1),(N,4),(W,1),(D)])
                    else:
                                
                                return([(A),(E,1),(N,4),(E,1),(D)])
        def checkB():
                    if s=='p':
                        pawn(s1)
                    elif s=='r':
                        Rook(s1)
                    elif s=='n':
                        Knight(s1)
                    elif s=='b':
                        Bishop(s1)
                    elif s=='q':
                        Queen(s1)
                    else:
                        King(s1)
        if isCapturing(BlackMove)==False:
                
                motor(a,b)
        checkB()
        

