from .models import Patient, Diagnostic, Segmentation
from rest_framework import serializers
from user import serializers as user_serializer

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'email', 'date_of_birth']
        
    def create(self, validated_data):
        patient = Patient(**validated_data)
        patient.save()
        return patient
    
    
class DiagnosticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnostic
        fields = ['id', 'patient', 'doctor', 'date_diagnostic', 'date_visit', 'diagnostic', 'note']
        
    def create(self, validated_data):
        diagnostic = Diagnostic(**validated_data)
        diagnostic.save()
        return diagnostic
    
    
class SegmentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Segmentation
        fields = ['id', 'patient', 'doctor', 'date_segmentation', 'original_image', 'segmented_image', 'note']
        
    def create(self, validated_data):
        segmentation = Segmentation(**validated_data)
        segmentation.save()
        return segmentation