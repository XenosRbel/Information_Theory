function lab2

x = [0, 3, 3, 3, 4, 5,  6,  7,  8,  7,  10, 11, 12, 13, 14, 15];
y = [0, 2, 4, 6, 8, 10, 12, 14, 16, 17, 20, 22, 24, 26, 28, 30];

plot(x,y,'-o');

B = length(x);
H = zeros(B,B);
for n = 1:B
	for v = 1:B
        H(n,v) = cos((2*pi*(v-1)*(n-1))/B)+sin((2*pi*(v-1)*(n-1))/B);
	end
end
disp('Table H:');
disp(H);

gx = zeros(B);
xl = x(1);
for t = 1:B
    gx(t) = cos((2*pi*abs(x(t)-xl)*(t-1))/B)+sin((2*pi*abs(x(t)-xl)*(t-1))/B);
    xl = x(t); 
end

gy = zeros(B);
yl = y(t);
for t = 1:B
    gy(t) = cos((2*pi*abs(y(t)-yl)*(t-1))/B)+sin((2*pi*abs(y(t)-yl)*(t-1))/B);
    yl = y(t); 
end

gv = (H*gx);
gu = (H*gy);

disp('gx:');
disp(gx);
disp('gvx:');
disp(gv);
disp('gy:');
disp(gy);
disp('gvy:');
disp(gu);



v = 9999;
for t = 1:B
    if(gv(t) == max(max(gv)))
        v = t-1;
    end
end

u = 9999;
for t = 1:B
    if(gu(t) == max(max(gu)))
        u = t-1;
    end
end
p = 1;
d = 1;

Vx = d*v*p;
Vy = d*u*p;
V = sqrt(Vx*Vx + Vy*Vy);
disp('v:');
disp(v);
disp('u');
disp(u);
disp('V:');
disp(V);


