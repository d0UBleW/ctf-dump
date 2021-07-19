# flag\_shop

```c
int number_flags = 0;
fflush(stdin);
scanf("%d", &number_flags);
if(number_flags > 0){
	int total_cost = 0;
	total_cost = 900*number_flags;
	printf("\nThe final cost is: %d\n", total_cost);
	if(total_cost <= account_balance){
		account_balance = account_balance - total_cost;
	}
}
```
Our aim is to make the value of `total_cost` to become negative by overflowing it . This is due to the signed data type of `int`. For example, if we input `number_flags` equal to `2**31`, when it is multiplied by 900, the resulting bits will be `11100000111111111111111111111110001111100` which is 41-bit long. However, the size of `int` data type is only 4 bytes (32 bits). Thus, it will only store that much, resulting `total_cost` value in binary become `11111111111111111111110001111100` which is equivalent to `-900` in 2's complement.

Note: make sure the 32nd bit (counting from LSB) is equal to `1` which indicates a negative value.
