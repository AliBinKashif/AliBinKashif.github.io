#include <stdio.h>
#include <stdbool.h>

#define MAXSTRINGSIZE 100

int Length(char *s){
	/*finds length of string*/
	int length = 0;

	while (*s != '\0'){
		length++;
		s++;
	}

	return length;

}



void Strncopy(char *s, char *t,int n){

	if (Length(s) < n){
		printf("length of string is less than %d\n", n);
	}else{

		/*copies the first n characters of string s and \0 to string t*/
		int i;
		for (i = 0; i < n; ++i){
			*(t+i) = *(s+i);
		}
		*(t+i) = '\0';
		

	}

}




/*adds the first n characters of string s and \n to string t*/
void Strncat(char *s, char *t, int n){

	/*if n is greater than the length of string s we give error*/
	if (Length(s) < n){

		printf("length of string to be concatenated is lesser than %d\n", n);

	}else{

		/*moves  pointer to end of string t*/
		while (*t != '\0'){
			++t;
		}

		if (Length(t) + n + 1 <= MAXSTRINGSIZE){
			int i;
			for (i = 0; i < n; ++i){
				*(t+i) = *(s+i);
			}
			*(t+i) = '\0';

		}else{
			printf("cannot cat; capacity of string exceeds max limit\n");
		}
	}
}




/*checks if the first n characters of both strings are the same*/
bool Strncmp(char *s, char *t, int n){

	if (Length(s) < n || Length(t) < n){
		printf("one of the strings is smaller than %d\n", n);
		return false;
	}else{

		for (int i = 0; i < n; ++i){

			if (*(t + i) != *(s + i)){
				return false;
			}

		}
		return true;

	}
}



void Input(char *s){
	/*takes input until string has less than max number of characters*/
	int length, i;
	bool exceed;
	do{
		exceed = false;
		length = 0;
		printf("enter the word you want to enter: ");
		int c;
		for (i = 0; (c = getchar()) != '\n'; ++i){
			*(s+i) = c;
			length++;
			if (length == MAXSTRINGSIZE){
				exceed = true;
				printf("max limit exceeded\n");
				while (c = getchar() != '\n');
				break;
			}
			
		}
	}while(exceed);
	*(s+i) = '\n';
}



int main(){
	char str1[MAXSTRINGSIZE], str2[MAXSTRINGSIZE];
	Input(str1);
	int n;
	printf("how many characters do you want to copy from the string: ");
	scanf("%d", &n);
	getchar();
	Strncopy(str1, str2, n);
	printf("%s\n", str2);

	char str3[MAXSTRINGSIZE], str4[MAXSTRINGSIZE];
	str4[0] = '\0';
	for (int i = 0; i < 3; i++){
		Input(str3);
		printf("how many characters do you want to cat from string: ");
		scanf("%d", &n);
		getchar();
		Strncat(str3, str4, n);
	}
	printf("%s\n", str4);

	char str5[MAXSTRINGSIZE], str6[MAXSTRINGSIZE];
	str5[0] = str6[0] = '\0';
	Input(str5);
	Input(str6);
	printf("how many characters of both strings should be the same: ");
	scanf("%d", &n);
	if (Strncmp(str5, str6, n)){
		printf("the first %d characters of both strigs are the same.\n", n);
	}else{
		printf("the first %d characters of both strigs are not the same.\n", n);
	}
	return 0;
}
