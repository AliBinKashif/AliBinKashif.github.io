#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>



void CreateAccount();
void Login();
void Deposit(int amount, int index);
void Withdraw(int amount, int index);
void Input();
bool Equal(char array1[], char array2[]);
void GetBalance(int index);



char userDataBase[10][2][25];
int userAccounts[12];
int users = 0;



void CreateAccount(){
	if (users == 10){
		printf("bank is full; we cant have more customers\n");
	}else{
		printf("enter your username \n");
		// adding user name
		char username[25];
		Input(username);
		int i;
		for (i = 0; username[i] != '\n'; ++i){
			userDataBase[users][0][i] = username[i];
		}
		userDataBase[users][0][i] = username[i];		
		//adding password
		bool equal = true;
		char temp1[25];
		char temp2[25];
		do{
			if (!equal){
				printf("passwords dont match, reenter!\n");
			}
			printf("enter a password\n");
			Input(temp1);
			printf("reenter your password\n");
			Input(temp2);
			equal = false;
		}while(!Equal(temp1, temp2));
		int k;
		for (k = 0; temp1[k] != '\n';++k){
			userDataBase[users][1][k] = temp1[k];
		}
		userDataBase[users][1][k] = temp1[k];
		++users;
	}
}


void Input(char temp[]){

	/*keeps taking Input till string has 24 characters or less; \n is added after the string*/
	bool success = false;
	while (!success){
		success = true;
		int i = 0;
		int c;
		while ((c = getchar()) != '\n' && i < 24){
			temp[i] = c;
			++i;
		}
		if (i == 24 && c != '\n'){
			success = false;
			printf("try again\n");
		}else{
			temp[i] = c;
		}
	}
}


bool Equal(char array1[], char array2[]){
	/*checks if two arrays are equal to one another: all elements of both array are same*/
	bool equal = true;
	int i;
	for (i = 0; array1[i] != '\n' || array2[i] != '\n'; ++i){
		if (array1[i] != array2[i]){
			equal = false;
			break;
		}
	}

	if (array1[i] != array2[i]){
		equal = false;
	}

	return equal;
}





void Login(){
	/*takes username as Input; checks if username is in date base; if yes then asks for password; user can enter password three times; if fail then we dont proceed*/
	printf("enter your username\n");
	char temp[25];
	Input(temp);
	bool found = false;
	int i;
	for (i = 0; i < users; i++){
		if (Equal(temp, userDataBase[i][0])){
			found = true;
			break;
		}
	}
	if (found){
		char password[25];
		bool equal = false;

		for (int j = 0; j < 3; ++j){
			printf("enter your password\n");
			Input(password);



			if (Equal(password, userDataBase[i][1])){
				/*if correct password entered, then we ask if they have to deposit or withdraw and do the required operation*/
				equal = true;
				int choice;
				printf("enter 1 to deposit, 2 to withdraw, and 3 to get current balance\n");
				while ((choice = getchar()) != '\n'){



					int amount;
					if (choice - '0' == 1){
						printf("how much do you want to deposit: \n");
						scanf("%d", &amount);
						Deposit(amount, i);
					}else if(choice - '0' == 2){
						printf("how much do you want to withdraw: \n");
						scanf("%d", &amount);
						Withdraw(amount, i);		
					}else if(choice - '0' == 3){
						GetBalance(i);
					}



				}
				break;
			}
		}



		if (!equal){
			printf("max tries completed\n");
		}



	}else{
		printf("username not found\n");
	}
}



void Deposit(int amount, int index){
	/*adds "amount" amount to account*/

	userAccounts[index]+= amount;
}



void Withdraw(int amount, int index){
	/*removes "amount" amount from account; if account does not have enough, only the amount present is withdrawn*/

	if (amount > userAccounts[index]){
		printf("you only have %d\n", userAccounts[index]);
		userAccounts[index] = 0;
	}else{
		userAccounts[index] -= amount;
	}
}



void GetBalance(int index){
	printf("you have %d\n", userAccounts[index]);		
}



int main(){
	for (int i = 0; i < 10; i++){
		userAccounts[i] = 0;
	}
	/*asks the user if they want to create a new account or login and then performs the required operation*/
	printf("enter 1 to login and 2 to create a new account\n");
	int choice;
	while ((choice = getchar()) != EOF){
		if (choice - '0' == 1){
			choice = getchar();
			Login();
		}else if (choice - '0' == 2){
			choice = getchar();
			CreateAccount();
		}
		printf("enter 1 to login and 2 to create a new account\n");
	}
	return 0;
}
