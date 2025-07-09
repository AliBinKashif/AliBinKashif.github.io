#include <stdio.h>
#include <ctype.h>
#define BUFFERSIZE 1000

int getch();
void ungetch(int);
int getint(int *);

int bufferArray[BUFFERSIZE];
int top;

int getch(){

	if (top > 0){
		return bufferArray[--top];
	}else{
		return getchar();
	}

}

void ungetch(int c){

	if (top == BUFFERSIZE){
		printf("cannot unget more characters at the moment.\n");
	}else{
		bufferArray[top] = c;
		++top;
	}

}

int getint(int *np){
	int c, sign;

	while (isspace(c = getch()));
	if (!isdigit(c) && c != EOF && c != '+' && c != '-'){
		/*this means c is not a number*/
		ungetch(c);
		return 0;
	}

	/*if there is nothing after + or - return 0*/
	if (c == '+' || c == '-'){
		int temp = c;
		c = getch();
		if (c == EOF || c == '\n'){
			ungetch(c);
			return 0;
		}
		ungetch(c);
		c = temp;
	}


	/*if there is a negative sign then the number is negative else positive*/
	sign = (c == '-') ? -1 : 1;
	if (c == '+' || c == '-'){
		c = getch();
	}
	for (*np = 0; isdigit(c); c = getch()){
		*np = *np *10 + (c - '0');
	}
	*np *= sign;
	if (c != EOF || c != '\n'){
		ungetch(c);
	}
	return c;
}

int main(){
	int i, c;
	top = 0;
	while ((c = getint(&i)) != EOF){
		if (c == 0){
			printf("not a number\n");
		}else if (c == '\n'){
			printf("%d\n", i);
			getch();
		}else{
			printf("%d\n", i);
		}
	}
}

