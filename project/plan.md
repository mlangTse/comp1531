# Plan of the group project. (Lang, Michael, Zack, Frank)
### In this project, we have 32 functions to implement:
* **Auth**: 5 (login, logout, register, password request, password reset)
* **Channel**: 10(invite, details, message, leave, join, addowner, removeowner, list, listall, create)
* **Message**: 7(sendlater, send, remove, edit, react, unreact, pin, unpin)
* **User**: 5(user profile, set name, set email, set handle, upload photo)
* **Stand**: 2(send, start)
* **Search**: 1
* **Admin**: 1(admin_userpermission_change)

### Depending on the object dealing with, we divide the 32 function into three parts: A, C, M.
* A includes auth, user, admin because they are all about the operation of accounts.
* C part only includes channel function itself because they are all about the operations of channel.
* M part includes message, stand, search because they are all about the operation of message.

## The normal process we implement each function is:
discussion->implementation->test, check, debug (by teammate).  

### Discussion
We will develop A part first because implementations of C part and M part are based on the account, furthermore, it will be easier to find bug if we implement A part first because we don't need to worry about the function from other part. For the same reason, we will do C part next, then is the M. Also, for the similar reason, we will do the functions which involve the smallest number of other functions at first for each part.
 We will try our best to ensure the current part has no bug before we move to the next part, which can make debugging more efficient. People in the team should always need to work in their own branch first and implement different function at same time to avoid merge conflict. For the same reason, we should pull and merge master in to our branch before we did any change on our branch.

### Implementation
During the implementation, we check the user stories and assumption all the time to make sure we don't head to the wrong track. It's also possible that we make new assumption during the implementation. Adding comment is also necessary in the team work, it can improve the overall efficient of communication.

### Test, Check, Debug
According to the plan, we will finish the implementation and debugging of A and C in the first week (week4), and finish the M part in second week (week 5), everybody should implement 8 functions (32 / 4 = 8 ) eventually. The time left will be used to final checking and optimization about system running time, coding style and the adding comment.

### Diagramatic plan:
![](https://i.ibb.co/yfnyYgY/71472461-2113254588774637-1997870687036899328-n.jpg)

