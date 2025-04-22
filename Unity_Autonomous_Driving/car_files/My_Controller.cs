using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class My_Controller : MonoBehaviour {

    private float MotorForce = 200.0f;
    private float SteerForce = 50.0f;
    public Transform centerOfMass;

    public WheelCollider FL;
    public WheelCollider FR;
    public WheelCollider BL;
    public WheelCollider BR;

    private Rigidbody myRigidbody; 


    void Start()
    {
        myRigidbody = GetComponent<Rigidbody>();
        myRigidbody.centerOfMass = centerOfMass.localPosition; 
    }

    void Update()
    {
        float v1 = Input.GetAxis("Vertical") * MotorForce;
        float v2 = Input.GetAxis("Horizontal") * SteerForce;
        FL.steerAngle = v2;
        FR.steerAngle = v2;

        BL.motorTorque = v1;
        BR.motorTorque = v1;
        FL.motorTorque = v1;
        FR.motorTorque = v1;
    }
}
