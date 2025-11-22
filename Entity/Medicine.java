package com.examly.entity;

public class Medicine {
    private int medicineId;
    private int pharmacyId;
    private String name;
    private double price;
    private String description;
    private int availableQuantity;

    public Medicine(){}

    public Medicine(int pharmacyId,String name,double price,String description,int availableQuantity)
    {
        this.pharmacyId = pharmacyId;
        this.name= name;
        this.price = price;
        this.description= description;
        this.availableQuantity= availableQuantity;
    }

    public Medicine(int medicineId,int pharmacyId,String name,double price,String description,int availableQuantity)
    {
        this.medicineId=medicineId;
        this.pharmacyId=pharmacyId;
        this.name=name;
        this.price=price;
        this.description = description;
        this.availableQuantity = availableQuantity;
    }
    public int getMedicineId()

    {
        return medicineId;
    }

    public void setMedicineId(int medicineId)
    {
        this.medicineId = medicineId;
    }
    public int getPharmacyId()
    {
        return pharmacyId;
    }
    public void setPharmacyId(int pharmacyId)
    {
        this.pharmacyId=pharmacyId;
    }
    public String getName()
    {
        return name;
    }
    public void setName(String name)
    {
        this.name = name;
    }
    public double getPrice()
    {
        return price;
    }
    public void setPrice(double price)
    {
        this.price = price;
    }
    public String getDescription()
    {
        return description;
    }
    public void setDescription(String description)
    {
        this.description = description;
    }
    public int getAvailableQuantity()
    {
        return availableQuantity;
    }
    public void setAvailableQuantity(int availableQuantity)
    {
        this.availableQuantity = availableQuantity;
    }

}
