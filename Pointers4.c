#include <stdio.h>
#include <stdbool.h>

#define STRINGLENGTH 10

bool strend(char *s, char *t){
	int lengthS = 0;
	int lengthT = 0;

	/*finds length of string s and moves pointer to end of string*/
	while (*s != '\0'){
		++s;
		lengthS++;
	}

	/*finds length of string t and moves pointer to end of string*/
	while (*t != '\0'){
		++t;
		lengthT++;
	}

	/*if length of t is greater than the length of s, it returns 0*/
	if (lengthT > lengthS){
		return 0;
	}
	
	/*if any character at the end of s for the length of t is not same we return false, else true*/
	for (int i = 0; i < lengthT; ++i){
		--s;
		--t;
		if (*s != *t){
			return false;
		}
		
	}
	return true;
}



void Input(char *s){
	int c, length;
	bool flag = false;
	char *temp = s;
	/*by default flag will be true but if length of string exceeds max, we loop again from start*/
	while (!flag){
		flag = true;
		printf("enter a word: ");
		length = 0;
		/*till we reach \n characters are read and input to array through pointer*/
		while ((c = getchar()) != '\n'){
			/*in case length exeeds we change s to start of string and set flag to false*/	
			if (length == STRINGLENGTH - 1){
				s = temp;
				flag = false;
				printf("maximum limit exceeded, try again.\n");
				while ((c = getchar()) != '\n');
				break;
			}else{
				*s = c;
				length++;
				++s;
			}
		}
		if (flag){
			/*this will be our method to determine end of string*/
			*s = '\0';
		}
	}
}



int main(){
	char string1[STRINGLENGTH], string2[STRINGLENGTH];
	Input(string1);
	Input(string2);
	if (strend(string1, string2)){
		printf("found\n");
	}else{
		printf("not found\n");
	}
	return 0;
}
