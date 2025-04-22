using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using Unity.MLAgents;
using Unity.MLAgents.Sensors;
using Unity.MLAgents.Actuators;
using UnityEngine;




public class CarAgent : Agent
{
    /*
    This script descirbes the behaviour of the agent car which shall learn to drive. Here are basics for the abilitiy of driving. Also a user is able to steer 
    and drive the car with help of the keyboard. To speed up the training process rewards/penalties are given for certain behaviour, e. g. reaching a 
    sub goal (tag=mark) or crush into an object like a tag=wall. Furhtermore, we descirbe sensors here which shall measure the distance between the agent 
    car and the surrounding objects (LIDAR). 

    The basics of steering and driving the designed car are a prefab given by the lecturer of this course. However, we also implemented ourselves a car agent
    with same functionality by following the seminar slides 'GettingStartedwithUnity'. However, for design reasons we have chosen this car here. 
    (If it is wished we can also exchange the two cars).
    The LIDAR implementation was inspired by the tutorial https://www.youtube.com/watch?v=CqcvfxOxNPk. The ability to collect LIDAR information with the 
    function vectorSensor.AddObservation() was applied from the slide deck concerning 'ML-Agent'. For implementing the LIDAR distance measure
    we followed the adivce of the lecturer.

    In the upcoming script the comments shall explain the functionality of it to transport a better understanding of what is happening.
     */

    // Define all public variables which can be also given directly in unity hub by the user:
    private float MotorForce = 200.0f;
    private float SteerForce = 50.0f;
    public Transform centerOfMass;
    //public Transform GoalO,GoalT;

    public WheelCollider FL;
    public WheelCollider FR;
    public WheelCollider BL;
    public WheelCollider BR;

    public float fcsx = 48.4f;
    public float fcsy = 2f;
    public float fcsz = -69f;

    private Rigidbody myRigidbody;
    private GameObject[] checkPoint;

    public int breakZeroOne = 0; // zero means our car can also drive backwards, 1 implies that the car has breaks but isn't able to drive backwards.

    [Header("Sensors")]
    public float frontsideSensorPosition = 0.6f; //half length of car
    public float sensorLength = 8f;

    public Vector3 frontSensorPosition = new Vector3(0.3f, 0.2f, 0.1f); // 0.5 as half of the length of car
    public float frontSensorAngle = 30;

    private float score = 0; // reached score by summing up all rewards/penalties

    void Start() // getting started with our script; will be used firstly each time when the scirpt is called
    {
        myRigidbody = this.GetComponent<Rigidbody>(); // the car agent's body is meant
        myRigidbody.centerOfMass = this.centerOfMass.localPosition;

        checkPoint = GameObject.FindGameObjectsWithTag("check"); // checkPoints are objects with 'check' as tag. Here the car gets a bonus for reaching them on the map.
    }

    public override void OnEpisodeBegin()
    {   // With starting of a new epsidoe reset the environment and car state:
        this.myRigidbody.angularVelocity = Vector3.zero;
        this.myRigidbody.velocity = Vector3.zero;
        this.transform.localPosition = new Vector3(85.02f, 2f, -107.0631f);//(53.76f, 1.00554f, -86.82f);
        this.transform.localEulerAngles = new Vector3(4.931f, -151.172f, 0.92f); //(0, -90, 0);
        FL.steerAngle = 0;
        FR.steerAngle = 0;
        BL.motorTorque = 0;
        BR.motorTorque = 0;
        FL.motorTorque = 0;
        FR.motorTorque = 0;

        for (int i = 0; i < checkPoint.Length; i++)
        {
            checkPoint[i].SetActive(true); //reset check points
        }

    }

    public override void CollectObservations(VectorSensor vectorSensor)
    {   // Here we want to collect the information of the LIDAR sensor which is also generated in this function


        RaycastHit hit; // needed for recognizing when a sensor line touches an object

        // Generate a vector which gives us the starting position of the sensor in the front of the car:
        Vector3 sensorStartPos = this.transform.position;
        sensorStartPos += this.transform.forward * frontSensorPosition.z;
        Vector3 v = new Vector3(0f, 0.3f, 0f); // the sensors shouldn't be to near to the ground, else they can react to the street ground. 
        sensorStartPos += this.transform.up * frontSensorPosition.y + v;


        float distance = 0; // how far the agent is away from the object
        float found = 1.633118f; // found in experiment: for frontal straight sensors we observed that they have at least a minimal distance of 
        // 1.633118 to other objects; substract that later to reach 0 distance; this could come because of the start of the sensor which is inside the agent

        // front sensor:
        if (Physics.Raycast(sensorStartPos, this.transform.forward, out hit, sensorLength)) // in brackets: (origin vector, vector of direction, maximal distance, length of sensor line),
                                                                                            // https://docs.unity3d.com/530/Documentation/ScriptReference/Physics.Raycast.html
                                                                                            // True if the ray intersects with a Collider, otherwise false.
        {
            
            UnityEngine.Debug.DrawLine(sensorStartPos, hit.point); //see sensor during playing simulation through 'Scene' tab

            distance = hit.distance - found;
            //UnityEngine.Debug.Log(distance); // get as output in the 'Console' window how far away a surrounding object is

            vectorSensor.AddObservation(distance); // we observe how far away the car is from a surrounding object;
            // https://docs.unity3d.com/Packages/com.unity.ml-agents@1.0/api/Unity.MLAgents.Sensors.VectorSensor.html
        }
                
        //right sensor:
        distance = 0;
        sensorStartPos += this.transform.right * frontsideSensorPosition; // shift starting position of right sensor to the right
        if (Physics.Raycast(sensorStartPos, this.transform.forward, out hit, sensorLength)) //transform.forward gives us the direction of the sensor
        {
            UnityEngine.Debug.DrawLine(sensorStartPos, hit.point);
            distance = hit.distance - found;
            // UnityEngine.Debug.Log(distance);

            vectorSensor.AddObservation(distance);
        }
        
        //right angular sensor:
        if (Physics.Raycast(sensorStartPos, Quaternion.AngleAxis(frontSensorAngle, this.transform.up) * this.transform.forward, out hit, sensorLength)) 
        {
            UnityEngine.Debug.DrawLine(sensorStartPos, hit.point);
            distance = hit.distance;
            //UnityEngine.Debug.Log(distance);
            vectorSensor.AddObservation(distance);
        }
        
        //left sensor:
        distance = 0;
        sensorStartPos -= this.transform.right * frontsideSensorPosition * 2;
        if (Physics.Raycast(sensorStartPos, this.transform.forward, out hit, sensorLength))
        {
            UnityEngine.Debug.DrawLine(sensorStartPos, hit.point);
            distance = hit.distance - found;
            //UnityEngine.Debug.Log(distance);
            vectorSensor.AddObservation(distance);
        }
                
        //left angular sensor:
        distance = 0;
        if (Physics.Raycast(sensorStartPos, Quaternion.AngleAxis(-frontSensorAngle, this.transform.up) * this.transform.forward, out hit, sensorLength))
        {
            UnityEngine.Debug.DrawLine(sensorStartPos, hit.point);
            distance = hit.distance - found;
            //UnityEngine.Debug.Log(distance);
            vectorSensor.AddObservation(distance);
        }
   
    }




    public override void OnActionReceived(ActionBuffers vectorAction) // What a car shall do when it gets the action commands.
                                                                      // When ActionBuffers is marked as incorrect then update your ML Agent package in the Package Manager
    {
        float v1 = vectorAction.ContinuousActions[0] * SteerForce;
        float v2 = vectorAction.ContinuousActions[1] * MotorForce;



        if (breakZeroOne == 1)
        {
            if (v2 < 0)
            {
                BL.brakeTorque = 300;
                BR.brakeTorque = 300;
                FL.brakeTorque = 300;
                FR.brakeTorque = 300;
            }
            else
            {
                BL.brakeTorque = 0;
                BR.brakeTorque = 0;
                FL.brakeTorque = 0;
                FR.brakeTorque = 0;

                FL.steerAngle = v1;
                FR.steerAngle = v1;

                BL.motorTorque = v2;
                BR.motorTorque = v2;
                FL.motorTorque = v2;
                FR.motorTorque = v2;
            }
        }
        else
        {
            FL.steerAngle = v1;
            FR.steerAngle = v1;

            BL.motorTorque = v2;
            BR.motorTorque = v2;
            FL.motorTorque = v2;
            FR.motorTorque = v2;
        }
        
        AddReward(-10f / MaxStep); //make the agent completes the task faster
        score -= 10f / MaxStep;
    }

    void OnCollisionEnter(Collision col) // What shall happen when the car agent drives into something
    {
        //UnityEngine.Debug.Log(col.gameObject.tag);
        if (col.gameObject.CompareTag("wall")) // car drives into a object with tag=wall
        {
            SetReward(-1.0f);
            score -= 1.0f;
            EndEpisode(); // Car agent has to start again at the starting postion with resetted environment and car knowledge
        }
        if (col.gameObject.CompareTag("Player"))
        {
            SetReward(-1.0f);
            score -= 1.0f;
            EndEpisode();
        }
        if (col.gameObject.CompareTag("Untagged"))
        {
            SetReward(-1.0f);
            score -= 1.0f;
            EndEpisode();
        }

    }

    void OnTriggerStay(Collider col)
    {
        if (col.gameObject.CompareTag("check") && myRigidbody.velocity != Vector3.zero) // subgoal is reached, a game object with tag=check which was placed by us
        {
            //UnityEngine.Debug.Log(col.gameObject.tag);
            col.gameObject.SetActive(false);
            // SetReward(1.0f);
            AddReward(1.0f);
            score += 1.0f;
        }
        else if (col.gameObject.CompareTag("goal") && myRigidbody.velocity != Vector3.zero)
        {
            //UnityEngine.Debug.Log(col.gameObject.tag);
            // SetReward(10.0f);
            AddReward(10.0f);
            score += 10.0f;
            EndEpisode(); // car finished the mission with success
        }
    }

    public override void Heuristic(in ActionBuffers actions) // User gets the opportunity to drive the car by herself/himself with help of the keyboard arrows
    {
        var actionsOut = actions.ContinuousActions;

        actionsOut[0] = Input.GetAxis("Horizontal");
        actionsOut[1] = Input.GetAxis("Vertical");
    }










}
