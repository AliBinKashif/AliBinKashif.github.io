#include <stdio.h>
#define MAXSTRINGSIZE 100
void Strcat(char *s, char *t){
	int lengths = 0;
	int lengtht = 0;
	while (*t != '\0'){
		++t;
		++lengtht;
	}
	char *temp = s;
	while (*temp != '\0'){
		++temp;
		++lengths;
	}
	if (lengths + lengtht >= MAXSTRINGSIZE - 1){
		printf("maxsize exceeded; cannot concatenate");
	}else{
		while (*s != '\0'){
			*t++ = *s++;
		}
		++t;
		*t = '\0';
		
	}
	
}



void Input(char *s){
	printf("enter a word: ");
	int c;
	while ((c = getchar()) != '\n'){
		*s = c;
		++s;
	}
	*s = '\0';
}

int main(){
	char string1[MAXSTRINGSIZE], string2[MAXSTRINGSIZE];
	string2[0] = '\0';
	for (int i = 0; i < 3; i++){
		Input(string1);
		Strcat(string1, string2);
	}
	printf("%s\n", string2);
	

	return 0;
}
