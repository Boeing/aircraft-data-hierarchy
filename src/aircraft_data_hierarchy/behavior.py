from __future__ import annotations
from datetime import date
from enum import Enum
from typing import List, Optional, Union
from pydantic import BaseModel, Field, field_validator, ValidationError, ValidationInfo

class CommonBaseModel(BaseModel):
    """Base model for all Pydantic models."""
    pass

class ExtrapolateEnum(str, Enum):
    NEITHER = "neither"
    MIN = "min"
    MAX = "max"
    BOTH = "both"

class InterpolateEnum(str, Enum):
    DISCRETE = "discrete"
    FLOOR = "floor"
    CEILING = "ceiling"
    LINEAR = "linear"
    QUADRATIC_SPLINE = "quadraticSpline"
    CUBIC_SPLINE = "cubicSpline"

class ContactInfoType(str, Enum):
    ADDRESS = "address"
    PHONE = "phone"
    FAX = "fax"
    EMAIL = "email"
    INAME = "iname"
    WEB = "web"

class ContactLocation(str, Enum):
    PROFESSIONAL = "professional"
    PERSONAL = "personal"
    MOBILE = "mobile"

class UncertaintyEffect(str, Enum):
    ADDITIVE = "additive"
    MULTIPLICATIVE = "multiplicative"
    PERCENTAGE = "percentage"
    ABSOLUTE = "absolute"

class Author(CommonBaseModel):
    """
    Represents an author of a DAVE-ML document.

    Attributes:
        name (Optional[str]): The name of the author.
        org (Optional[str]): The organization the author belongs to.
        xns (Optional[str]): The XNS identifier for the author.
        email (Optional[str]): The email address of the author.
        address (Optional[List[str]]): The physical address of the author.
        contact_info (Optional[List[ContactInfo]]): Additional contact information for the author.
    """
    name: Optional[str] = Field(None, description="The name of the author")
    org: Optional[str] = Field(None, description="The organization the author belongs to")
    xns: Optional[str] = Field(None, description="The XNS identifier for the author")
    email: Optional[str] = Field(None, description="The email address of the author")
    address: Optional[List[str]] = Field(None, description="The physical address of the author")
    contact_info: Optional[List[ContactInfo]] = Field(None, description="Additional contact information for the author")

class ContactInfo(CommonBaseModel):
    """
    Represents contact information for an author.

    Attributes:
        value (Optional[str]): The contact information value.
        contact_info_type (Optional[ContactInfoType]): The type of contact information.
        contact_location (Optional[ContactLocation]): The location associated with the contact information.
    """
    value: Optional[str] = Field(None, description="The contact information value")
    contact_info_type: Optional[ContactInfoType] = Field(None, description="The type of contact information")
    contact_location: Optional[ContactLocation] = Field(None, description="The location associated with the contact information")

class CreationDate(CommonBaseModel):
    """
    Represents the creation date of a DAVE-ML document.

    Attributes:
        date (Optional[date]): The creation date in ISO 8601 format (YYYY-MM-DD).
    """
   #date: Optional[date] = Field(None, description="The creation date in ISO 8601 format (YYYY-MM-DD)")
    date: Optional[date]

class FileVersion(CommonBaseModel):
    """
    Represents the version of a DAVE-ML document.

    Attributes:
        value (Optional[str]): The version string.
    """
    value: Optional[str] = Field(None, description="The version string")

class Description(CommonBaseModel):
    """
    Represents a textual description of an entity.

    Attributes:
        value (Optional[str]): The description text.
    """
    value: Optional[str] = Field(None, description="The description text")

class Reference(CommonBaseModel):
    """
    Represents a reference to an external document.

    Attributes:
        ref_id (Optional[str]): The unique identifier for this reference.
        author (Optional[str]): The author of the referenced document.
        title (Optional[str]): The title of the referenced document.
        classification (Optional[str]): The classification of the referenced document.
        accession (Optional[str]): The accession number of the referenced document.
        date (Optional[date]): The publication date of the referenced document.
        href (Optional[str]): The URL of the referenced document.
        description (Optional[Description]): A description of the referenced document.
    """
    ref_id: Optional[str] = Field(None, description="The unique identifier for this reference")
    author: Optional[str] = Field(None, description="The author of the referenced document")
    title: Optional[str] = Field(None, description="The title of the referenced document")
    classification: Optional[str] = Field(None, description="The classification of the referenced document")
    accession: Optional[str] = Field(None, description="The accession number of the referenced document")
   #date: Optional[date] = Field(None, description="The publication date of the referenced document")
    date: Optional[date]
    href: Optional[str] = Field(None, description="The URL of the referenced document")
    description: Optional[Description] = Field(None, description="A description of the referenced document")

class ModificationRecord(CommonBaseModel):
    """
    Represents a modification record for a DAVE-ML document.

    Attributes:
        mod_id (Optional[str]): The unique identifier for this modification record.
        date (Optional[date]): The date of the modification.
        ref_id (Optional[str]): The reference ID associated with this modification.
        author (Optional[List[Author]]): The authors of the modification.
        description (Optional[Description]): A description of the modification.
        extra_doc_ref (Optional[List[ExtraDocRef]]): Additional document references.
    """
    mod_id: Optional[str] = Field(None, description="The unique identifier for this modification record")
   #date: Optional[date] = Field(None, description="The date of the modification")
    date: Optional[date]
    ref_id: Optional[str] = Field(None, description="The reference ID associated with this modification")
    author: Optional[List[Author]] = Field(None, description="The authors of the modification")
    description: Optional[Description] = Field(None, description="A description of the modification")
    extra_doc_ref: Optional[List[ExtraDocRef]] = Field(None, description="Additional document references")

class ExtraDocRef(CommonBaseModel):
    """
    Represents an additional document reference.

    Attributes:
        ref_id (Optional[str]): The reference ID of the additional document.
    """
    ref_id: Optional[str] = Field(None, description="The reference ID of the additional document")

class Provenance(CommonBaseModel):
    """
    Represents the provenance of a DAVE-ML document or element.

    Attributes:
        prov_id (Optional[str]): The unique identifier for this provenance record.
        author (Optional[List[Author]]): The authors associated with this provenance.
        creation_date (Optional[CreationDate]): The creation date of the associated element.
        document_ref (Optional[List[DocumentRef]]): References to related documents.
        modification_ref (Optional[List[ModificationRef]]): References to related modifications.
        description (Optional[Description]): A description of the provenance.
    """
    prov_id: Optional[str] = Field(None, description="The unique identifier for this provenance record")
    author: Optional[List[Author]] = Field(None, description="The authors associated with this provenance")
    creation_date: Optional[CreationDate] = Field(None, description="The creation date of the associated element")
    document_ref: Optional[List[DocumentRef]] = Field(None, description="References to related documents")
    modification_ref: Optional[List[ModificationRef]] = Field(None, description="References to related modifications")
    description: Optional[Description] = Field(None, description="A description of the provenance")

class ProvenanceRef(CommonBaseModel):
    """
    Represents a reference to a provenance record.

    Attributes:
        prov_id (Optional[str]): The ID of the referenced provenance record.
    """
    prov_id: Optional[str] = Field(None, description="The ID of the referenced provenance record")

class DocumentRef(CommonBaseModel):
    """
    Represents a reference to a document.

    Attributes:
        doc_id (Optional[str]): The ID of the referenced document.
        ref_id (Optional[str]): The reference ID of the document.
    """
    doc_id: Optional[str] = Field(None, description="The ID of the referenced document")
    ref_id: Optional[str] = Field(None, description="The reference ID of the document")

class ModificationRef(CommonBaseModel):
    """
    Represents a reference to a modification record.

    Attributes:
        mod_id (Optional[str]): The ID of the referenced modification record.
    """
    mod_id: Optional[str] = Field(None, description="The ID of the referenced modification record")

class Calculation(CommonBaseModel):
    """
    Represents a calculation using MathML content markup.

    Attributes:
        math (Optional[str]): The MathML content markup describing the calculation.
    """
    math: Optional[str] = Field(None, description="The MathML content markup describing the calculation")

class Uncertainty(CommonBaseModel):
    """
    Represents the uncertainty of a function or parameter value.

    Attributes:
        effect (Optional[UncertaintyEffect]): The effect of the uncertainty.
        normal_pdf (Optional[NormalPDF]): The normal probability distribution function.
        uniform_pdf (Optional[UniformPDF]): The uniform probability distribution function.
    """
    effect: Optional[UncertaintyEffect] = Field(None, description="The effect of the uncertainty")
    normal_pdf: Optional[NormalPDF] = Field(None, description="The normal probability distribution function")
    uniform_pdf: Optional[UniformPDF] = Field(None, description="The uniform probability distribution function")

    @field_validator('normal_pdf', 'uniform_pdf')
    def validate_pdf(cls, v, info: ValidationInfo):
        if v is not None and info.data.get('normal_pdf') and info.data.get('uniform_pdf'):
            raise ValueError("Only one of normal_pdf or uniform_pdf can be specified")
        return v

class NormalPDF(CommonBaseModel):
    """
    Represents a normal probability distribution function.

    Attributes:
        num_sigmas (Optional[float]): The number of standard deviations.
        bounds (Optional[List[Bounds]]): The bounds of the distribution.
        correlates_with (Optional[List[CorrelatesWith]]): Correlations with other variables.
        correlation (Optional[List[Correlation]]): Correlation coefficients.
    """
    num_sigmas: Optional[float] = Field(None, description="The number of standard deviations")
    bounds: Optional[List[Bounds]] = Field(None, description="The bounds of the distribution")
    correlates_with: Optional[List[CorrelatesWith]] = Field(None, description="Correlations with other variables")
    correlation: Optional[List[Correlation]] = Field(None, description="Correlation coefficients")

class UniformPDF(CommonBaseModel):
    """
    Represents a uniform probability distribution function.

    Attributes:
        bounds (Optional[List[Bounds]]): The bounds of the distribution.
    """
    bounds: Optional[List[Bounds]] = Field(None, min_items=1, description="The bounds of the distribution")

class Bounds(CommonBaseModel):
    """
    Represents the statistical limits of a parameter.

    Attributes:
        value (Optional[Union[str, DataTable, VariableDef, VariableRef]]): The bound value or reference.
    """
    value: Optional[Union[str, DataTable, VariableDef, VariableRef]] = Field(None, description="The bound value or reference")

class CorrelatesWith(CommonBaseModel):
    """
    Indicates correlation with another variable.

    Attributes:
        var_id (Optional[str]): The ID of the correlated variable.
    """
    var_id: Optional[str] = Field(None, description="The ID of the correlated variable")

class Correlation(CommonBaseModel):
    """
    Represents a correlation between variables.

    Attributes:
        var_id (Optional[str]): The ID of the correlated variable.
        corr_coef (Optional[float]): The correlation coefficient.
    """
    var_id: Optional[str] = Field(None, description="The ID of the correlated variable")
    corr_coef: Optional[float] = Field(None, description="The correlation coefficient")

class VariableDef(CommonBaseModel):
    """
    Represents the definition of a variable.

    Attributes:
        name (Optional[str]): The name of the variable.
        var_id (Optional[str]): The unique identifier for this variable.
        units (Optional[str]): The units of measure for the variable.
        axis_system (Optional[str]): The axis system for the variable.
        sign (Optional[str]): The sign convention for the variable.
        alias (Optional[str]): An alias for the variable.
        symbol (Optional[str]): A symbol representing the variable.
        initial_value (Optional[float]): The initial value of the variable.
        min_value (Optional[float]): The minimum allowed value of the variable.
        max_value (Optional[float]): The maximum allowed value of the variable.
        description (Optional[Description]): A description of the variable.
        provenance (Optional[Provenance]): The provenance of the variable.
        provenance_ref (Optional[ProvenanceRef]): A reference to the provenance of the variable.
        calculation (Optional[Calculation]): The calculation for deriving the variable's value.
        is_input (Optional[bool]): Indicates if the variable is an input.
        is_control (Optional[bool]): Indicates if the variable is a control parameter.
        is_disturbance (Optional[bool]): Indicates if the variable is a disturbance input.
        is_state (Optional[bool]): Indicates if the variable is a state variable.
        is_state_deriv (Optional[bool]): Indicates if the variable is a state derivative.
        is_output (Optional[bool]): Indicates if the variable is an output.
        is_std_aiaa (Optional[bool]): Indicates if the variable is a standard AIAA variable.
        uncertainty (Optional[Uncertainty]): The uncertainty associated with the variable.
    """
    name: Optional[str] = Field(None, description="The name of the variable")
    var_id: Optional[str] = Field(None, description="The unique identifier for this variable")
    units: Optional[str] = Field(None, description="The units of measure for the variable")
    axis_system: Optional[str] = Field(None, description="The axis system for the variable")
    sign: Optional[str] = Field(None, description="The sign convention for the variable")
    alias: Optional[str] = Field(None, description="An alias for the variable")
    symbol: Optional[str] = Field(None, description="A symbol representing the variable")
    initial_value: Optional[float] = Field(None, description="The initial value of the variable")
    min_value: Optional[float] = Field(None, description="The minimum allowed value of the variable")
    max_value: Optional[float] = Field(None, description="The maximum allowed value of the variable")
    description: Optional[Description] = Field(None, description="A description of the variable")
    provenance: Optional[Provenance] = Field(None, description="The provenance of the variable")
    provenance_ref: Optional[ProvenanceRef] = Field(None, description="A reference to the provenance of the variable")
    calculation: Optional[Calculation] = Field(None, description="The calculation for deriving the variable's value")
    is_input: Optional[bool] = Field(None, description="Indicates if the variable is an input")
    is_control: Optional[bool] = Field(None, description="Indicates if the variable is a control parameter")
    is_disturbance: Optional[bool] = Field(None, description="Indicates if the variable is a disturbance input")
    is_state: Optional[bool] = Field(None, description="Indicates if the variable is a state variable")
    is_state_deriv: Optional[bool] = Field(None, description="Indicates if the variable is a state derivative")
    is_output: Optional[bool] = Field(None, description="Indicates if the variable is an output")
    is_std_aiaa: Optional[bool] = Field(None, description="Indicates if the variable is a standard AIAA variable")
    uncertainty: Optional[Uncertainty] = Field(None, description="The uncertainty associated with the variable")

class VariableRef(CommonBaseModel):
    """
    Represents a reference to a variable.

    Attributes:
        var_id (Optional[str]): The ID of the referenced variable.
    """
    var_id: Optional[str] = Field(None, description="The ID of the referenced variable")

class BreakpointDef(CommonBaseModel):
    """
    Represents the definition of a breakpoint set.

    Attributes:
        name (Optional[str]): The name of the breakpoint set.
        bp_id (Optional[str]): The unique identifier for this breakpoint set.
        units (Optional[str]): The units of measure for the breakpoints.
        description (Optional[Description]): A description of the breakpoint set.
        bp_vals (Optional[str]): The breakpoint values.
    """
    name: Optional[str] = Field(None, description="The name of the breakpoint set")
    bp_id: Optional[str] = Field(None, description="The unique identifier for this breakpoint set")
    units: Optional[str] = Field(None, description="The units of measure for the breakpoints")
    description: Optional[Description] = Field(None, description="A description of the breakpoint set")
    bp_vals: Optional[str] = Field(None, description="The breakpoint values")

class GriddedTableDef(CommonBaseModel):
    """
    Represents the definition of a gridded table.

    Attributes:
        name (Optional[str]): The name of the gridded table.
        gt_id (Optional[str]): The unique identifier for this gridded table.
        units (Optional[str]): The units of measure for the table values.
        description (Optional[Description]): A description of the gridded table.
        provenance (Optional[Provenance]): The provenance of the gridded table.
        provenance_ref (Optional[ProvenanceRef]): A reference to the provenance of the gridded table.
        breakpoint_refs (Optional[List[BpRef]]): References to the breakpoint sets used in this table.
        uncertainty (Optional[Uncertainty]): The uncertainty associated with the table values.
        data_table (Optional[DataTable]): The actual data of the gridded table.
    """
    name: Optional[str] = Field(None, description="The name of the gridded table")
    gt_id: Optional[str] = Field(None, description="The unique identifier for this gridded table")
    units: Optional[str] = Field(None, description="The units of measure for the table values")
    description: Optional[Description] = Field(None, description="A description of the gridded table")
    provenance: Optional[Provenance] = Field(None, description="The provenance of the gridded table")
    provenance_ref: Optional[ProvenanceRef] = Field(None, description="A reference to the provenance of the gridded table")
    breakpoint_refs: Optional[List[BpRef]] = Field(None, description="References to the breakpoint sets used in this table")
    uncertainty: Optional[Uncertainty] = Field(None, description="The uncertainty associated with the table values")
    data_table: Optional[DataTable] = Field(None, description="The actual data of the gridded table")

class UngriddedTableDef(CommonBaseModel):
    """
    Represents the definition of an ungridded table.

    Attributes:
        name (Optional[str]): The name of the ungridded table.
        ut_id (Optional[str]): The unique identifier for this ungridded table.
        units (Optional[str]): The units of measure for the table values.
        description (Optional[Description]): A description of the ungridded table.
        provenance (Optional[Provenance]): The provenance of the ungridded table.
        provenance_ref (Optional[ProvenanceRef]): A reference to the provenance of the ungridded table.
        uncertainty (Optional[Uncertainty]): The uncertainty associated with the table values.
        data_point (Optional[List[DataPoint]]): The data points of the ungridded table.
    """
    name: Optional[str] = Field(None, description="The name of the ungridded table")
    ut_id: Optional[str] = Field(None, description="The unique identifier for this ungridded table")
    units: Optional[str] = Field(None, description="The units of measure for the table values")
    description: Optional[Description] = Field(None, description="A description of the ungridded table")
    provenance: Optional[Provenance] = Field(None, description="The provenance of the ungridded table")
    provenance_ref: Optional[ProvenanceRef] = Field(None, description="A reference to the provenance of the ungridded table")
    uncertainty: Optional[Uncertainty] = Field(None, description="The uncertainty associated with the table values")
    data_point: Optional[List[DataPoint]] = Field(None, description="The data points of the ungridded table")

class Function(CommonBaseModel):
    """
    Represents a function in the DAVE-ML model.

    Attributes:
        name (Optional[str]): The name of the function.
        description (Optional[Description]): A description of the function.
        provenance (Optional[Provenance]): The provenance of the function.
        provenance_ref (Optional[ProvenanceRef]): A reference to the provenance of the function.
        independent_var_pts (Optional[List[IndependentVarPts]]): The independent variable points for simple functions.
        dependent_var_pts (Optional[DependentVarPts]): The dependent variable points for simple functions.
        independent_var_ref (Optional[List[IndependentVarRef]]): References to independent variables for complex functions.
        dependent_var_ref (Optional[DependentVarRef]): Reference to the dependent variable for complex functions.
        function_defn (Optional[FunctionDefn]): The function definition for complex functions.
    """
    name: Optional[str] = Field(None, description="The name of the function")
    description: Optional[Description] = Field(None, description="A description of the function")
    provenance: Optional[Provenance] = Field(None, description="The provenance of the function")
    provenance_ref: Optional[ProvenanceRef] = Field(None, description="A reference to the provenance of the function")
    independent_var_pts: Optional[List[IndependentVarPts]] = Field(None, description="The independent variable points for simple functions")
    dependent_var_pts: Optional[DependentVarPts] = Field(None, description="The dependent variable points for simple functions")
    independent_var_ref: Optional[List[IndependentVarRef]] = Field(None, description="References to independent variables for complex functions")
    dependent_var_ref: Optional[DependentVarRef] = Field(None, description="Reference to the dependent variable for complex functions")
    function_defn: Optional[FunctionDefn] = Field(None, description="The function definition for complex functions")

    @field_validator('dependent_var_pts', 'dependent_var_ref', 'function_defn')
    def validate_function_type(cls, v, info: ValidationInfo):
        if v is not None:
            if info.data.get('independent_var_pts') and info.data.get('independent_var_ref'):
                raise ValueError("Function can't have both simple and complex representations")
        return v

class Function(BaseModel):
    name: str
    description: Optional[str] = None
    simple_representation: Union[DependentVarRef, None] = Field(None, alias="dependent_var_ref")
    complex_representation: Union[FunctionDefn, None] = Field(None, alias="function_defn")

    @field_validator('simple_representation', 'complex_representation')
    def check_representation(cls, v, values):
        if v is not None and 'simple_representation' in values and 'complex_representation' in values:
            if values['simple_representation'] is not None and values['complex_representation'] is not None:
                raise ValueError("Function can't have both simple and complex representations")
        return v

class IndependentVarPts(CommonBaseModel):
    """
    Represents independent variable points for a simple function.

    Attributes:
        var_id (Optional[str]): The ID of the referenced variable.
        name (Optional[str]): The name of the independent variable.
        units (Optional[str]): The units of the independent variable.
        sign (Optional[str]): The sign convention for the independent variable.
        extrapolate (Optional[ExtrapolateEnum]): The extrapolation method.
        interpolate (Optional[InterpolateEnum]): The interpolation method.
        value (Optional[str]): The values of the independent variable points.
    """
    var_id: Optional[str] = Field(None, description="The ID of the referenced variable")
    name: Optional[str] = Field(None, description="The name of the independent variable")
    units: Optional[str] = Field(None, description="The units of the independent variable")
    sign: Optional[str] = Field(None, description="The sign convention for the independent variable")
    extrapolate: Optional[ExtrapolateEnum] = Field(None, description="The extrapolation method")
    interpolate: Optional[InterpolateEnum] = Field(None, description="The interpolation method")
    value: Optional[str] = Field(None, description="The values of the independent variable points")

class DependentVarPts(CommonBaseModel):
    """
    Represents dependent variable points for a simple function.

    Attributes:
        var_id (Optional[str]): The ID of the referenced variable.
        name (Optional[str]): The name of the dependent variable.
        units (Optional[str]): The units of the dependent variable.
        sign (Optional[str]): The sign convention for the dependent variable.
        value (Optional[str]): The values of the dependent variable points.
    """
    var_id: Optional[str] = Field(None, description="The ID of the referenced variable")
    name: Optional[str] = Field(None, description="The name of the dependent variable")
    units: Optional[str] = Field(None, description="The units of the dependent variable")
    sign: Optional[str] = Field(None, description="The sign convention for the dependent variable")
    value: Optional[str] = Field(None, description="The values of the dependent variable points")

class IndependentVarRef(CommonBaseModel):
    """
    Represents a reference to an independent variable for a complex function.

    Attributes:
        var_id (Optional[str]): The ID of the referenced variable.
        min (Optional[float]): The minimum value of the independent variable.
        max (Optional[float]): The maximum value of the independent variable.
        extrapolate (Optional[ExtrapolateEnum]): The extrapolation method.
        interpolate (Optional[InterpolateEnum]): The interpolation method.
    """
    var_id: Optional[str] = Field(None, description="The ID of the referenced variable")
    min: Optional[float] = Field(None, description="The minimum value of the independent variable")
    max: Optional[float] = Field(None, description="The maximum value of the independent variable")
    extrapolate: Optional[ExtrapolateEnum] = Field(None, description="The extrapolation method")
    interpolate: Optional[InterpolateEnum] = Field(None, description="The interpolation method")

class DependentVarRef(CommonBaseModel):
    """
    Represents a reference to a dependent variable for a complex function.

    Attributes:
        var_id (Optional[str]): The ID of the referenced variable.
    """
    var_id: Optional[str] = Field(None, description="The ID of the referenced variable")

class FunctionDefn(CommonBaseModel):
    """
    Represents the definition of a complex function.

    Attributes:
        name (Optional[str]): The name of the function definition.
        gridded_table_ref (Optional[GriddedTableRef]): A reference to a gridded table.
        gridded_table_def (Optional[GriddedTableDef]): A gridded table definition.
        gridded_table (Optional[GriddedTable]): A gridded table.
        ungridded_table_ref (Optional[UngriddedTableRef]): A reference to an ungridded table.
        ungridded_table_def (Optional[UngriddedTableDef]): An ungridded table definition.
        ungridded_table (Optional[UngriddedTable]): An ungridded table.
    """
    name: Optional[str] = Field(None, description="The name of the function definition")
    gridded_table_ref: Optional[GriddedTableRef] = Field(None, description="A reference to a gridded table")
    gridded_table_def: Optional[GriddedTableDef] = Field(None, description="A gridded table definition")
    gridded_table: Optional[GriddedTable] = Field(None, description="A gridded table")
    ungridded_table_ref: Optional[UngriddedTableRef] = Field(None, description="A reference to an ungridded table")
    ungridded_table_def: Optional[UngriddedTableDef] = Field(None, description="An ungridded table definition")
    ungridded_table: Optional[UngriddedTable] = Field(None, description="An ungridded table")

    @field_validator('gridded_table_ref', 'gridded_table_def', 'gridded_table', 'ungridded_table_ref', 'ungridded_table_def', 'ungridded_table')
    def validate_table_type(cls, v, info: ValidationInfo):
        if v is not None:
            table_fields = ['gridded_table_ref', 'gridded_table_def', 'gridded_table', 'ungridded_table_ref', 'ungridded_table_def', 'ungridded_table']
            if sum(1 for field in table_fields if info.data.get(field) is not None) > 1:
                raise ValueError("Only one table type can be specified in a function definition")
        return v

class GriddedTableRef(CommonBaseModel):
    """
    Represents a reference to a gridded table.

    Attributes:
        gt_id (Optional[str]): The ID of the referenced gridded table.
    """
    gt_id: Optional[str] = Field(None, description="The ID of the referenced gridded table")

class GriddedTable(CommonBaseModel):
    """
    Represents a gridded table.

    Attributes:
        name (Optional[str]): The name of the gridded table.
        breakpoint_refs (Optional[List[BpRef]]): References to the breakpoint sets used in this table.
        confidence_bound (Optional[ConfidenceBound]): The confidence bound for the table data.
        data_table (Optional[DataTable]): The actual data of the gridded table.
    """
    name: Optional[str] = Field(None, description="The name of the gridded table")
    breakpoint_refs: Optional[List[BpRef]] = Field(None, description="References to the breakpoint sets used in this table")
    confidence_bound: Optional[ConfidenceBound] = Field(None, description="The confidence bound for the table data")
    data_table: Optional[DataTable] = Field(None, description="The actual data of the gridded table")

class UngriddedTableRef(CommonBaseModel):
    """
    Represents a reference to an ungridded table.

    Attributes:
        ut_id (Optional[str]): The ID of the referenced ungridded table.
    """
    ut_id: Optional[str] = Field(None, description="The ID of the referenced ungridded table")

class UngriddedTable(CommonBaseModel):
    """
    Represents an ungridded table.

    Attributes:
        name (Optional[str]): The name of the ungridded table.
        confidence_bound (Optional[ConfidenceBound]): The confidence bound for the table data.
        data_point (Optional[List[DataPoint]]): The data points of the ungridded table.
    """
    name: Optional[str] = Field(None, description="The name of the ungridded table")
    confidence_bound: Optional[ConfidenceBound] = Field(None, description="The confidence bound for the table data")
    data_point: Optional[List[DataPoint]] = Field(None, description="The data points of the ungridded table")

class BpRef(CommonBaseModel):
    """
    Represents a reference to a breakpoint set.

    Attributes:
        bp_id (Optional[str]): The ID of the referenced breakpoint set.
    """
    bp_id: Optional[str] = Field(None, description="The ID of the referenced breakpoint set")

class ConfidenceBound(CommonBaseModel):
    """
    Represents a confidence bound for table data.

    Attributes:
        value (Optional[float]): The value of the confidence bound.
    """
    value: Optional[float] = Field(None, description="The value of the confidence bound")

class DataTable(CommonBaseModel):
    """
    Represents the actual data of a gridded table.

    Attributes:
        value (Optional[str]): The table data as a string of comma- or whitespace-separated values.
    """
    value: Optional[str] = Field(None, description="The table data as a string of comma- or whitespace-separated values")

class DataPoint(CommonBaseModel):
    """
    Represents a data point in an ungridded table.

    Attributes:
        mod_id (Optional[str]): The ID of the modification record for this data point.
        value (Optional[str]): The values of the data point.
    """
    mod_id: Optional[str] = Field(None, description="The ID of the modification record for this data point")
    value: Optional[str] = Field(None, description="The values of the data point")

class CheckData(CommonBaseModel):
    """
    Represents check data for model verification.

    Attributes:
        provenance (Optional[Provenance]): The provenance of the check data.
        provenance_ref (Optional[ProvenanceRef]): A reference to the provenance of the check data.
        static_shot (Optional[List[StaticShot]]): Static check cases.
    """
    provenance: Optional[Provenance] = Field(None, description="The provenance of the check data")
    provenance_ref: Optional[ProvenanceRef] = Field(None, description="A reference to the provenance of the check data")
    static_shot: Optional[List[StaticShot]] = Field(None, description="Static check cases")

class StaticShot(CommonBaseModel):
    """
    Represents a static check case.

    Attributes:
        name (Optional[str]): The name of the static shot.
        ref_id (Optional[str]): The reference ID for this static shot.
        description (Optional[Description]): A description of the static shot.
        provenance (Optional[Provenance]): The provenance of the static shot.
        provenance_ref (Optional[ProvenanceRef]): A reference to the provenance of the static shot.
        check_inputs (Optional[CheckInputs]): The input values for this check case.
        internal_values (Optional[InternalValues]): The internal variable values for this check case.
        check_outputs (Optional[CheckOutputs]): The expected output values for this check case.
    """
    name: Optional[str] = Field(None, description="The name of the static shot")
    ref_id: Optional[str] = Field(None, description="The reference ID for this static shot")
    description: Optional[Description] = Field(None, description="A description of the static shot")
    provenance: Optional[Provenance] = Field(None, description="The provenance of the static shot")
    provenance_ref: Optional[ProvenanceRef] = Field(None, description="A reference to the provenance of the static shot")
    check_inputs: Optional[CheckInputs] = Field(None, description="The input values for this check case")
    internal_values: Optional[InternalValues] = Field(None, description="The internal variable values for this check case")
    check_outputs: Optional[CheckOutputs] = Field(None, description="The expected output values for this check case")

class CheckInputs(CommonBaseModel):
    """
    Represents the input values for a check case.

    Attributes:
        signal (Optional[List[Signal]]): The input signals for this check case.
    """
    signal: Optional[List[Signal]] = Field(None, description="The input signals for this check case")

class InternalValues(CommonBaseModel):
    """
    Represents the internal variable values for a check case.

    Attributes:
        signal (Optional[List[Signal]]): The internal signals for this check case.
    """
    signal: Optional[List[Signal]] = Field(None, description="The internal signals for this check case")

class CheckOutputs(CommonBaseModel):
    """
    Represents the expected output values for a check case.

    Attributes:
        signal (Optional[List[Signal]]): The output signals for this check case.
    """
    signal: Optional[List[Signal]] = Field(None, description="The output signals for this check case")

class Signal(CommonBaseModel):
    """
    Represents a signal (input, internal, or output) in a check case.

    Attributes:
        signal_name (Optional[str]): The name of the signal.
        signal_units (Optional[str]): The units of the signal.
        var_id (Optional[str]): The ID of the variable associated with this signal.
        signal_value (Optional[str]): The value of the signal.
        tol (Optional[str]): The tolerance for this signal's value.
    """
    signal_name: Optional[str] = Field(None, description="The name of the signal")
    signal_units: Optional[str] = Field(None, description="The units of the signal")
    var_id: Optional[str] = Field(None, description="The ID of the variable associated with this signal")
    signal_value: Optional[str] = Field(None, description="The value of the signal")
    tol: Optional[str] = Field(None, description="The tolerance for this signal's value")

class DAVEfunc(CommonBaseModel):
    """
    Represents the root element of a DAVE-ML document.

    Attributes:
        file_header (Optional[FileHeader]): The header information for the DAVE-ML document.
        variable_def (Optional[List[VariableDef]]): The variable definitions in the document.
        breakpoint_def (Optional[List[BreakpointDef]]): The breakpoint set definitions in the document.
        gridded_table_def (Optional[List[GriddedTableDef]]): The gridded table definitions in the document.
        ungridded_table_def (Optional[List[UngriddedTableDef]]): The ungridded table definitions in the document.
        function (Optional[List[Function]]): The function definitions in the document.
        check_data (Optional[CheckData]): The check data for model verification.
    """
    file_header: Optional[FileHeader] = Field(None, description="The header information for the DAVE-ML document")
    variable_def: Optional[List[VariableDef]] = Field(None, description="The variable definitions in the document")
    breakpoint_def: Optional[List[BreakpointDef]] = Field(None, description="The breakpoint set definitions in the document")
    gridded_table_def: Optional[List[GriddedTableDef]] = Field(None, description="The gridded table definitions in the document")
    ungridded_table_def: Optional[List[UngriddedTableDef]] = Field(None, description="The ungridded table definitions in the document")
    function: Optional[List[Function]] = Field(None, description="The function definitions in the document")
    check_data: Optional[CheckData] = Field(None, description="The check data for model verification")

class FileHeader(CommonBaseModel):
    """
    Represents the header information for a DAVE-ML document.

    Attributes:
        name (Optional[str]): The name of the DAVE-ML document.
        author (Optional[List[Author]]): The authors of the document.
        creation_date (Optional[CreationDate]): The creation date of the document.
        file_version (Optional[FileVersion]): The version of the document.
        description (Optional[Description]): A description of the document.
        reference (Optional[List[Reference]]): References to external documents.
        modification_record (Optional[List[ModificationRecord]]): Records of modifications to the document.
        provenance (Optional[List[Provenance]]): Provenance information for the document.
    """
    name: Optional[str] = Field(None, description="The name of the DAVE-ML document")
    author: Optional[List[Author]] = Field(None, description="The authors of the document")
    creation_date: Optional[CreationDate] = Field(None, description="The creation date of the document")
    file_version: Optional[FileVersion] = Field(None, description="The version of the document")
    description: Optional[Description] = Field(None, description="A description of the document")
    reference: Optional[List[Reference]] = Field(None, description="References to external documents")
    modification_record: Optional[List[ModificationRecord]] = Field(None, description="Records of modifications to the document")
    provenance: Optional[List[Provenance]] = Field(None, description="Provenance information for the document")

# Update forward references
Author.update_forward_refs()
Provenance.update_forward_refs()
FunctionDefn.update_forward_refs()
GriddedTableDef.update_forward_refs()
UngriddedTableDef.update_forward_refs()
Function.update_forward_refs()
GriddedTable.update_forward_refs()
UngriddedTable.update_forward_refs()
CheckData.update_forward_refs()
StaticShot.update_forward_refs()
DAVEfunc.update_forward_refs()

# This section describes the Sequence, Activity, state describing Behavior of Systems

class ActivityState(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class Activity(CommonBaseModel):
    """
    Represents an individual activity or task within a project's workflow, detailing the necessary steps or processes.

    Attributes:
        name (Optional[str]): A unique name identifying the activity.
        description (Optional[str]): A brief description of the activity's purpose and objectives.
        state (Optional[ActivityState]): The current state of the activity.
        dependencies (Optional[List[str]]): A list of activity names that this activity depends on.
        metadata (Optional[Metadata]): Additional metadata providing further context or details about the activity.

    Raises:
        ValueError: If essential string attributes are empty, ensuring all activities are descriptive and actionable.
    """
    name: Optional[str] = Field(None, description="A unique name identifying the activity.")
    description: Optional[str] = Field(None, description="A brief description of the activity's purpose and objectives.")
    state: Optional[ActivityState] = Field(None, description="The current state of the activity.")
    dependencies: Optional[List[str]] = Field(None, description="List of activity names that this activity depends on.")
    metadata: Optional[Metadata] = Field(None, description="Additional metadata for the activity.")

    @field_validator('name', 'description')
    def validate_non_empty(cls, value: str) -> str:
        """Validates that the name and description fields are not empty or whitespace only."""
        if value is not None and not value.strip():
            raise ValueError("Name and description fields must not be empty.")
        return value

    @field_validator('dependencies')
    def validate_dependency_names(cls, value: List[str]) -> List[str]:
        """Validates that dependency names are not empty and are valid strings."""
        if value is not None:
            for item in value:
                if not item.strip():
                    raise ValueError("Dependency names must not be empty or just whitespace.")
        return value

class Behavior(CommonBaseModel):
    """
    Represents the behavioral model of a system or project, detailing the sequence and interrelations of activities.

    This class provides a structured approach to describe how various components or systems within a project
    behave or interact over time, through a sequence of defined activities.

    Attributes:
        name (Optional[str]): The name of the behavior, serving as a unique identifier.
        description (Optional[str]): A brief description of the behavior, providing context or purpose.
        sequence (Optional[List[Activity]]): A list of activities that constitute the behavior sequence,
                                             ordered by their execution or dependency relation.
        metadata (Optional[Metadata]): Additional metadata providing further context or details about the behavior.

    Raises:
        ValueError: If essential attributes are empty or if the sequence does not contain at least one activity.
    """
    name: Optional[str] = Field(None, description="A unique name identifying the behavior.")
    description: Optional[str] = Field(None, description="A brief description of the behavior.")
    sequence: Optional[List[Activity]] = Field(None, description="A sequence of activities that define the behavior.")
    metadata: Optional[Metadata] = Field(None, description="Additional metadata providing context about the behavior.")

    @field_validator("name", "description", mode="before")
    def validate_non_empty(cls, value: str) -> str:
        """Validates that the name and description fields are not empty or whitespace only.

        Args:
            value: The value of the field being validated.

        Returns:
            The validated string value.

        Raises:
            ValueError: If the input value is empty or consists only of whitespace.
        """
        if value is not None and not value.strip():
            raise ValueError("Name and description fields must not be empty.")
        return value

    @field_validator("sequence", mode="before")
    def validate_sequence(cls, value: List[Activity]) -> List[Activity]:
        """Validates that the sequence contains at least one activity.

        Args:
            value: The list of activities to validate.

        Returns:
            The validated list of activities.

        Raises:
            ValueError: If the sequence is empty.
        """
        if value is not None and not value:
            raise ValueError("The behavior sequence must contain at least one activity.")
        return value

class Metadata(CommonBaseModel):
    """
    Represents additional metadata for an activity or behavior.

    Attributes:
        key (Optional[str]): The key of the metadata.
        value (Optional[str]): The value of the metadata.
    """
    key: Optional[str] = Field(None, description="The key of the metadata")
    value: Optional[str] = Field(None, description="The value of the metadata")