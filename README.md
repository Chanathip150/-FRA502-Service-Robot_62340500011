# -FRA502-Service-Robot_62340500011


นาย ชนาธิป พุ่มพันธฺุุ์ 62340500011 

Vido test

https://drive.google.com/file/d/1QeqNEAQyTpxzMDgSOmEjmXH9-sWj_Ae4/view?usp=sharing 

วิธีการเปิด 
1. เปิด Gaxebo +spawn Robot
    roslaunch urdf_sim gazebo.launch
2. เปิด rviz + Autonomous Navigation
    roslaunch urdf_sim amcl_move_base.launch
3. คำสั่งเสียง Speech
    rosrun urdf_sim Mobi_move.py 
    คำสั่ง "a" ไปห้อง 1 
         "b" ไปห้อง 2 
         "c" ไปห้อง 3 
         "d" ไปห้อง 4 
         "f" ไปห้อง 5 
     
ปัญหาที่พบในการทำโปรเจคในครั้งนี้
1. บ้างครั้ง Gazebo หรือ คำสั่งต่างๆที่ใช้เกิดการ Bug บ้างครั้งไม่รู้สาเหตุเเต่สามารถปิดเเละเปิดเครื่องใหม่ก็จะใช้ได้
2. ในการทำงาน Navigation หุ่นยนต์จะเดินไม่ถูกหรือบางที่เกิด bug
3. เวลาสั่งคำสั่งเสียงเเล้วไปที่ห้องเเรกที่สั่ง ต่อจากนี้ทำให้ไม่สามารถสั่งคำสั่งต่อไปได้ เพราะเมื่อหุ่นยนต์เข้าไปในห้องเเล้วเเต่หุ่นยนต์ยังหาตำเเหน่งที่ตั้งไว้ไม่เจอจะสั่งต่อไม่ได้ซึ้งการหานั้นจะนาน
4. ในตอนนี้ยังไปได้เเค่ 1 ห้องเท่านั้น 
