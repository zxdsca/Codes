package com.examly.entity;
import java.sql.Date;

public class Payment {
    private int paymentId;
    private int orderId;
    private Date paymentDate;
    private String paymentStatus;
    private double amountPaid;

    public Payment(){}

    public Payment(int orderId,Date paymentDate,String paymentStatus,double amountPaid)
    {
        this.orderId = orderId;
        this.paymentDate=paymentDate;
        this.paymentStatus=paymentStatus;
        this.amountPaid=amountPaid;
    }

    public Payment(int paymentId,int orderId,Date paymentDate,String paymentStatus,double amountPaid)
    {
        this.paymentId=paymentId;
        this.orderId = orderId;
        this.paymentDate=paymentDate;
        this.paymentStatus=paymentStatus;
        this.amountPaid=amountPaid;
    }
    public int getPaymentId()
    {
        return paymentId;
    }
    public void setPayment(int paymentId)
    {
        this.paymentId = paymentId;
    }
    public int getOrderId()
    {
        return orderId;
    }
    public void setOrderId(int orderId)
    {
        this.orderId = orderId;
    }

    public Date getPaymentDate(){
        return paymentDate;
    }
    public void setPaymentDate(Date paymentDate)
    {
        this.paymentDate=paymentDate;
    }
    public String getPaymentStatus()
    {
        return paymentStatus;
    }
    public void setPaymentStatus(String paymentStatus)
    {
        this.paymentStatus=paymentStatus;
    }
    public double getAmountPaid()
    {
        return amountPaid;
    }
    public void setAmountPaid(double amountPaid)
    {
        this.amountPaid=amountPaid;
    }
}
