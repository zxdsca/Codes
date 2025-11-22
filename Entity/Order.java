package com.examly.entity;

public class Order {
        private int orderId;
        private int customerId;
        private int pharmacyId;
        private String orderStatus;
        private double totalPrice;
        private String deliveryAddress;

        public Order(){}

        public Order(int customerId,int pharmacyId,String orderStatus,double totalPrice,String deliveryAddress)
        {
                this.customerId=customerId;
                this.pharmacyId=pharmacyId;
                this.orderStatus=orderStatus;
                this.totalPrice=totalPrice;
                this.deliveryAddress=deliveryAddress;
        }

        public Order(int orderId,int customerId,int pharmacyId,String orderStatus,double totalPrice,String deliveryAddress)
        {
                this.orderId = orderId;
                this.customerId=customerId;
                this.pharmacyId=pharmacyId;
                this.orderStatus=orderStatus;
                this.totalPrice=totalPrice;
                this.deliveryAddress=deliveryAddress;
        }

        public int getOrderId()
        {
                return orderId;
        }
        public void setOrderId(int orderId)
        {
                this.orderId=orderId;
        }
        public int getCustomerId()
        {
                return customerId;
        }
        public void setCustomerId(int customerId)
        {
                this.customerId=customerId;
        }

        public int getPharmacyId()
        {
                return pharmacyId;
        }
        public void setPharmacyId(int pharmacyId)
        {
                this.pharmacyId=pharmacyId;
        }
        public String getOrderStatus()
        {
                return orderStatus;
        }
        public void setOrderStatus(String orderStatus)
        {
                this.orderStatus=orderStatus;
        }
        public double getTotalPrice()
        {
                return totalPrice;
        }

        public void setTotalPrice(double totalPrice)
        {
                this.totalPrice = totalPrice;
        }

        public String getDeliveryAddress()
        {
                return deliveryAddress;
        }
        public void setDeliveryAddress(String deliveryAddress)
        {
                this.deliveryAddress=deliveryAddress;
        }
}
