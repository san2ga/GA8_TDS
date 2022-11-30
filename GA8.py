import streamlit as st
header = st.container()
userinput = st.container()
output = st.container()

with header:
	st.title('welcome to my project')
	st.subheader('USECASE: Product of two given number')

with userinput:
	st.subheader('please enter the input')
	st.text('the output is a * b')
	num1 = st.number_input(label="enter a",step=1.,formate="%.2f")
	num2 = st.number_input(label="enter b",step=1.,formate="%.2f")

def prod(num1,num2):
	ans = num1	* num2
	return ans
ans = prod(num1,num2)

with output:
	st.subheader('please see the output below :')
	st.markdown(f'Answer is{ans}')	
