package com.examly.entity;

public class Pharmacy {
    private int pharmacyId;
    private String name;
    private String address;
    private String licenseNumber;
    private String contactNumber; 

    public Pharmacy(){}

    public Pharmacy(String name,String address,String licenseNumber,String contactNumber)
    {
        this.name=name;
        this.address=address;
        this.licenseNumber=licenseNumber;
        this.contactNumber=contactNumber;
    }
    public Pharmacy(int pharmacyId,String name,String address,String licenseNumber,String contactNumber)
    {
        this.pharmacyId=pharmacyId;
        this.name=name;
        this.address=address;
        this.licenseNumber=licenseNumber;
        this.contactNumber=contactNumber;
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
    public String getAddress()
    {
    return address;
    }
    public void setAddress(String address)
    {
    this.address=address;
    }
    public String getLicenseNumber()
    {
    return licenseNumber;
    }
    public void setLicenseNumber(String licenseNumber)
    {
    this.licenseNumber=licenseNumber;
    }
    public String getContactNumber()
    {
    return contactNumber;
    }
    public void setContactNumber(String contactNumber)
    {
    this.contactNumber=contactNumber;
    }
}
