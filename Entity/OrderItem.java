package com.examly.entity;

public class OrderItem {
     private int orderId;
     private int medicineId;
     private int quantity;

     public OrderItem(){}

     public OrderItem(int orderId, int medicineId, int quantity)
     {
          this.orderId=orderId;
          this.medicineId=medicineId;
          this.quantity = quantity;
     }

     public int getOrderId()
     {
          return orderId;
     }
     public void setOrderId(int orderId) 
     {
          this.orderId=orderId;
     }
     public int getMedicineId()
     {
          return medicineId;
     }
     public void setMedicineId(int medicineId) 
     {
          this.medicineId=medicineId;
     }
     public int getQuantity()
     {
          return quantity;
     
     }
     public void setQuantity(int quantity)
     {
          this.quantity = quantity;
     }

}
