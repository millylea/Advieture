# Advieture

A booking travel website made with Django and Python and Intergration Automation Test
## 1. Web pages


![Screenshot 2024-07-19 084406](https://github.com/user-attachments/assets/c0ba57f9-be4c-4f87-a2fa-0e38eb409b4a)
![Screenshot 2024-07-19 084530](https://github.com/user-attachments/assets/8284cb30-6129-481e-9f66-bf0b416b17b0)
![Screenshot 2024-07-19 084601](https://github.com/user-attachments/assets/602d532c-082d-4af1-8614-96f12acf7e5d)
![Screenshot 2024-07-19 084618](https://github.com/user-attachments/assets/b1396601-27b9-4999-a0a3-e8c438b8236f)
![Screenshot 2024-07-19 084705](https://github.com/user-attachments/assets/288c0aaf-5ea0-4229-8710-4f490be65bb5)
![Screenshot 2024-07-19 084729](https://github.com/user-attachments/assets/06e4cf92-d462-4414-9158-b3802d596ffd)
![Screenshot 2024-07-19 084815](https://github.com/user-attachments/assets/72c8f985-a504-4423-bf1b-f0a4eb7c3382)
![Screenshot 2024-07-19 084907](https://github.com/user-attachments/assets/a4e5b1b4-dfc8-42cb-8d57-b5a019bf1251)
![Screenshot 2024-07-19 084943](https://github.com/user-attachments/assets/9415add3-c205-4459-ae84-b0aa5677112e)
![Screenshot 2024-07-19 085056](https://github.com/user-attachments/assets/02dcf9e7-17e8-42d4-aa9a-62c9921faf70)
![Screenshot 2024-07-19 085110](https://github.com/user-attachments/assets/89f5ce88-a11c-4fe8-aa20-2e83921c3885)
![Screenshot 2024-07-19 085137](https://github.com/user-attachments/assets/df071b98-210b-4d02-a633-e110844e9067)

## 2. Karate Automation Test.

   To run this test, you must have [Karate set up](https://github.com/karatelabs/karate?tab=readme-ov-file#quickstart)

   Use Git Bash if you are curently using Powershell.
   
   ### Command lines:
- To run whole test:
  ```
  mvn test
  ```
- To run a certain feature or scenario, put a @debug tag before it:
  ```
  mvn test -Dkarate.options="--tags @debug"
  ```
- To run a whole test but skip a certain feature or scenario, put a @skipme tag before it:
  ```
  mvn test -Dkarate.options="--tags ~~@skipme"
  ```
   Reports are automaticly generated in "target/karate-report" and "target/cucumber-html" folder after each test run.
  
  ![Screenshot 2024-07-22 092513](https://github.com/user-attachments/assets/6c59508a-a0bd-4f8b-9a82-c0a55bd1f0fe)

  ![Screenshot 2024-07-22 093830](https://github.com/user-attachments/assets/cf88b2af-976e-4ca9-9f12-7f835835f229)



   
   
   
