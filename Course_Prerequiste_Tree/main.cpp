#include <iostream>
#include <fstream>
#include<stdio.h>
#include <string>
#include<ctype.h>
#include <bits/stdc++.h>
using namespace std;
int number = 0;
class node
{
public :
    int data;
    node *left;
    node *right;
    node()
    {
        left=right=NULL;
    }
};
class nodeforqueue
{
public :
    int data;
    nodeforqueue *next;
    nodeforqueue()
    {
        next=NULL;
    }
};
class queueusinglist
{
public :
    nodeforqueue *top,*tail;
    queueusinglist()
    {
        top=NULL;
        tail=NULL;
    }
    void enqueue(int value)
    {
        nodeforqueue *newnode = new nodeforqueue();
        newnode->data=value;
        newnode->next=NULL;
        if(top==NULL)
        {
            tail=top=newnode;
        }
        else
        {
            tail->next=newnode;
            tail=newnode;
        }
    }
    int dequeue()
    {
        if(top==NULL)
        {
            cout<<"queue Underflow.";
        }
        else
        {
            int x;
            if(top==tail)
            {
                x=top->data;
                free(top);
                top=tail=NULL;
                return x;
            }
            else
            {
                x=top->data;
                nodeforqueue *ptr = top;
                top=top->next;
                delete(ptr);
                return x;
            }
        }

    }

} ;
class queueusinglist2
{
public :
    nodeforqueue *top,*tail;
    queueusinglist2()
    {
        top=NULL;
        tail=NULL;
    }
    void enqueue(int value)
    {
        nodeforqueue *newnode = new nodeforqueue();
        newnode->data=value;
        newnode->next=NULL;
        if(top==NULL)
        {
            tail=top=newnode;
        }
        else
        {
            tail->next=newnode;
            tail=newnode;
        }
    }
    int dequeue()
    {
        if(top==NULL)
        {
            cout<<"queue Underflow.";
        }
        else
        {
            int x;
            if(top==tail)
            {
                x=top->data;
                free(top);
                top=tail=NULL;
                return x;
            }
            else
            {
                x=top->data;
                nodeforqueue *ptr = top;
                top=top->next;
                delete(ptr);
                return x;
            }
        }

    }

} ;
class tree
{
private :
    node *root;
public :
    tree()
    {
        root=NULL;
    }
    void addcoursehelper(int value, int value2, node *ptr)
    {
            node *newnode = new node();
            newnode->data=value;
            if(ptr==NULL)
            {
                return;
            }
            addcoursehelper(value,value2,ptr->left);
            if(ptr->data==value2)
            {
                if(ptr->left==NULL)
                {
                    ptr->left=newnode;
                }
                else
                {
                    ptr->right=newnode;
                }

            }
            addcoursehelper(value,value2,ptr->right);
    }
    void add(int value, int value2=0){
		if (value2==0){
        node *newnode = new node();
        newnode->data=value;
        root = newnode;
		}
		else{
			addcoursehelper(value,value2,root);
		}
	}
	 void preorder(node* temp){
		if (temp == NULL)
			return;

		cout << temp->data << " ";
		preorder(temp->left);
		preorder(temp->right);

	}
	 void display_preOrder(){
		if (root != NULL)
			preorder(root);

		cout << endl;
	}
    void searchtreehelper(int value,int value2,node*ptr)
	{
	        if(ptr==NULL)
            {
                return;
            }
            searchtreehelper(value,value2,ptr->left);
            if(ptr->data==value)
            {
               if(ptr->left!=NULL&&ptr->left->data==value2)
               {
                   number++;
                   if(number>0)
                   {
                   cout<<"\nYou can take "<<value2<<" course.";
                   }
               }
               if(ptr->right!=NULL&&ptr->right->data==value2)
               {
                   number++;
                   if(number>0)
                   {
                   cout<<"\nYou can take "<<value2<<" course.";
                   }
               }
            }
            searchtreehelper(value,value2,ptr->right);
	}
	void search(int value, int value2)
	{
	    if(root->data==value2)
        {
            cout<<"\nYou can take "<<value2<<" course.";
            number++;
        }
        else
        {
        searchtreehelper(value,value2,root);
        }
	}
};

int main()
{
 queueusinglist obj1;
 queueusinglist2 obj2;
 printf("%75s","Welcome To The Registering System.\n");
 tree obj;
 fstream projectfile;
 int counter = 0;
 projectfile.open("coursenames.txt",ios::in);
 if(projectfile.is_open())
 {
     string word;
     string subword;
     while(getline(projectfile,word))
     {
         int n,m;
         subword=word.substr(word.find(",") + 1);
         n=stoi(word);
         if(counter==0)
         {
             obj.add(n);
             counter++;
         }
         else
         {
             m=stoi(subword);
             obj.add(n,m);
         }
     }
     projectfile.close();
 }
 while(1)
 {
     cout<<"\n1-Register\n2-Exit";
     cout<<"\n\nEnter your choice : ";
     string x;
     getline(cin,x);
     if(x=="1")
     {
        cout<<"\nEnter the courses you took  (Hint: Enter stop to complete.) ";
         string z;
         while(1)
         {
             cout<<"\nEnter : ";
             getline(cin,z);
             if(z=="stop")
                break;
             obj1.enqueue(stoi(z));
         }
         cout<<"\nEnter the courses you want to take  (Hint; Enter stop to complete.) ";
         while(1)
         {
             cout<<"\nEnter : ";
             getline(cin,z);
              if(z=="stop")
                break;
             obj2.enqueue(stoi(z));
         }
         cout<<"\n\nprocessing......\n";
         nodeforqueue *ptr = obj1.top;
         nodeforqueue *ptr1 = obj2.top;
         while(ptr1!=NULL)
         {
             if(ptr==NULL)
             {
                 obj.search(0,ptr1->data);
             }
             while(ptr!=NULL)
             {
                 obj.search(ptr->data,ptr1->data);
                 ptr=ptr->next;
             }
             if(number==0)
             {
                  cout<<"\nYou can't take "<<ptr1->data<<" course.";
             }
             number = 0;
             ptr1=ptr1->next;
             ptr=obj1.top;
         }
         cout<<"\n";
         while(obj1.top!=NULL)
         {
             obj1.dequeue();
         }
         while(obj2.top!=NULL)
         {
             obj2.dequeue();
         }
     }
     if(x=="2")
        return 0;

 }
}
