from pydantic import BaseModel, Field, field_validator, Extra
from typing import Optional

# ToDo: 
# 1. Get airframe working for the Nacelle demo
# 2. Complete inheritance for all the other airframe components
# 3. Get propulsion working for Propulsion demo
# 4. Complete inheritance for all the other propulsion components
# 5. Get systems working for Systems demo
# 6. Complete inheritance for all the other systems components 
# 7. Flesh out equipment branch
# 8. Get equipment working for Equipment demo
# 9. Add any Operating items not covered by airframe, propulsion, systems, or equipment 
# 10. Complete inheritance for all the other operating items 
# 11. Demonstrate traversing branches to create weights buildup
# 12. Demonstrate traversing branches to create CG buildup
# 13. Demonstrate traversing branches to create weight based cost buildup
# 14. Demonstrate traversing branches to create parasite drag buildup
# 15. Create PINs from part locations and WBS structure
# 16. Demonstrate traversing branches to create part based cost buildup

from ..common_base_model import CommonBaseModel, Metadata
from .airframe.airframe import Component
#from .propulsion.propulsion import propulsion
#from .systems.systems import system
#from .equipment import * # Currently a local file

"""
Work Breakdown Structure Reference

1. [MIL-STD-881F Work Breakdown Structures for Defense Materiel Items](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=36026)
2. [SAWE RP A-8, 2015a: Weight and Balance Data Reporting Forms for Aircraft (including Rotorcraft and Air-Breathing Unmanned Aerial Vehicles)](https://www.sawe.org/product/sawe-rp-a-8-2015a/)

"""

class AircraftSystem(CommonBaseModel):
    wbs_no: Optional[str] = Field('1.0')

    @field_validator('wbs_no')
    def validate_wbs_no(cls, value: str) -> str:
        if not value.startswith('1.') or len(value) < 3:
            raise ValueError(f"Invalid WBS number: {value}")
        return value

    class Config:
        validate_assignment = True
        extra = 'allow'

    class AircraftSystemIntegrationAssemblyTestAndCheckout(CommonBaseModel):
        wbs_no: Optional[str] = Field('1.1')

        @field_validator('wbs_no')
        def validate_wbs_no(cls, value: str) -> str:
            if not value.startswith('1.'):
                raise ValueError(f'Invalid WBS number: {value}')
            return value

        class Config:
            validate_assignment = True
            extra = 'allow'

    class AirVehicle(CommonBaseModel):
        wbs_no: Optional[str] = Field('1.2')

        @field_validator('wbs_no')
        def validate_wbs_no(cls, value: str) -> str:
            if not value.startswith('1.'):
                raise ValueError(f'Invalid WBS number: {value}')
            return value

        class Config:
            validate_assignment = True
            extra = 'allow'

        class AirVehicleIntegrationAssemblyTestAndCheckout(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.2.1')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

        class Airframe(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.2.2')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

            class AirframeIntegrationAssemblyTestAndCheckout(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.2.1')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class Fuselage(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.2.2')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

                class BasicStructure(CommonBaseModel):
                    wbs_no: Optional[str] = Field('1.2.2.2.1')

                    @field_validator('wbs_no')
                    def validate_wbs_no(cls, value: str) -> str:
                        if not value.startswith('1.'):
                            raise ValueError(f'Invalid WBS number: {value}')
                        return value

                    class Config:
                        validate_assignment = True
                        extra = 'allow'

                    class Skins(CommonBaseModel):
                        wbs_no: Optional[str] = Field('1.2.2.2.1.1')

                        @field_validator('wbs_no')
                        def validate_wbs_no(cls, value: str) -> str:
                            if not value.startswith('1.'):
                                raise ValueError(f'Invalid WBS number: {value}')
                            return value

                        class Config:
                            validate_assignment = True
                            extra = 'allow'

                    class Stringers(CommonBaseModel):
                        wbs_no: Optional[str] = Field('1.2.2.2.1.2')

                        @field_validator('wbs_no')
                        def validate_wbs_no(cls, value: str) -> str:
                            if not value.startswith('1.'):
                                raise ValueError(f'Invalid WBS number: {value}')
                            return value

                        class Config:
                            validate_assignment = True
                            extra = 'allow'

                    class Frames(CommonBaseModel):
                        wbs_no: Optional[str] = Field('1.2.2.2.1.3')

                        @field_validator('wbs_no')
                        def validate_wbs_no(cls, value: str) -> str:
                            if not value.startswith('1.'):
                                raise ValueError(f'Invalid WBS number: {value}')
                            return value

                        class Config:
                            validate_assignment = True
                            extra = 'allow'

                    class Clips(CommonBaseModel):
                        wbs_no: Optional[str] = Field('1.2.2.2.1.4')

                        @field_validator('wbs_no')
                        def validate_wbs_no(cls, value: str) -> str:
                            if not value.startswith('1.'):
                                raise ValueError(f'Invalid WBS number: {value}')
                            return value

                        class Config:
                            validate_assignment = True
                            extra = 'allow'

                    class Beams(CommonBaseModel):
                        wbs_no: Optional[str] = Field('1.2.2.2.1.5')

                        @field_validator('wbs_no')
                        def validate_wbs_no(cls, value: str) -> str:
                            if not value.startswith('1.'):
                                raise ValueError(f'Invalid WBS number: {value}')
                            return value

                        class Config:
                            validate_assignment = True
                            extra = 'allow'

                    class Floors(CommonBaseModel):
                        wbs_no: Optional[str] = Field('1.2.2.2.1.6')

                        @field_validator('wbs_no')
                        def validate_wbs_no(cls, value: str) -> str:
                            if not value.startswith('1.'):
                                raise ValueError(f'Invalid WBS number: {value}')
                            return value

                        class Config:
                            validate_assignment = True
                            extra = 'allow'

                    class Bulkheads(CommonBaseModel):
                        wbs_no: Optional[str] = Field('1.2.2.2.1.7')

                        @field_validator('wbs_no')
                        def validate_wbs_no(cls, value: str) -> str:
                            if not value.startswith('1.'):
                                raise ValueError(f'Invalid WBS number: {value}')
                            return value

                        class Config:
                            validate_assignment = True
                            extra = 'allow'

                    class Longerons(CommonBaseModel):
                        wbs_no: Optional[str] = Field('1.2.2.2.1.8')

                        @field_validator('wbs_no')
                        def validate_wbs_no(cls, value: str) -> str:
                            if not value.startswith('1.'):
                                raise ValueError(f'Invalid WBS number: {value}')
                            return value

                        class Config:
                            validate_assignment = True
                            extra = 'allow'

                    class Supports(CommonBaseModel):
                        wbs_no: Optional[str] = Field('1.2.2.2.1.9')

                        @field_validator('wbs_no')
                        def validate_wbs_no(cls, value: str) -> str:
                            if not value.startswith('1.'):
                                raise ValueError(f'Invalid WBS number: {value}')
                            return value

                        class Config:
                            validate_assignment = True
                            extra = 'allow'

                class SecondaryStructure(CommonBaseModel):
                    wbs_no: Optional[str] = Field('1.2.2.2.2')

                    @field_validator('wbs_no')
                    def validate_wbs_no(cls, value: str) -> str:
                        if not value.startswith('1.'):
                            raise ValueError(f'Invalid WBS number: {value}')
                        return value

                    class Config:
                        validate_assignment = True
                        extra = 'allow'

                    class Enclosures(CommonBaseModel):
                        wbs_no: Optional[str] = Field('1.2.2.2.2.1')

                        @field_validator('wbs_no')
                        def validate_wbs_no(cls, value: str) -> str:
                            if not value.startswith('1.'):
                                raise ValueError(f'Invalid WBS number: {value}')
                            return value

                        class Config:
                            validate_assignment = True
                            extra = 'allow'

                    class Flooring(CommonBaseModel):
                        wbs_no: Optional[str] = Field('1.2.2.2.2.2')

                        @field_validator('wbs_no')
                        def validate_wbs_no(cls, value: str) -> str:
                            if not value.startswith('1.'):
                                raise ValueError(f'Invalid WBS number: {value}')
                            return value

                        class Config:
                            validate_assignment = True
                            extra = 'allow'

                    class Partitions(CommonBaseModel):
                        wbs_no: Optional[str] = Field('1.2.2.2.2.3')

                        @field_validator('wbs_no')
                        def validate_wbs_no(cls, value: str) -> str:
                            if not value.startswith('1.'):
                                raise ValueError(f'Invalid WBS number: {value}')
                            return value

                        class Config:
                            validate_assignment = True
                            extra = 'allow'

                    class Windows(CommonBaseModel):
                        wbs_no: Optional[str] = Field('1.2.2.2.2.4')

                        @field_validator('wbs_no')
                        def validate_wbs_no(cls, value: str) -> str:
                            if not value.startswith('1.'):
                                raise ValueError(f'Invalid WBS number: {value}')
                            return value

                        class Config:
                            validate_assignment = True
                            extra = 'allow'

                    class Doors(CommonBaseModel):
                        wbs_no: Optional[str] = Field('1.2.2.2.2.5')

                        @field_validator('wbs_no')
                        def validate_wbs_no(cls, value: str) -> str:
                            if not value.startswith('1.'):
                                raise ValueError(f'Invalid WBS number: {value}')
                            return value

                        class Config:
                            validate_assignment = True
                            extra = 'allow'

                    class Ramps(CommonBaseModel):
                        wbs_no: Optional[str] = Field('1.2.2.2.2.6')

                        @field_validator('wbs_no')
                        def validate_wbs_no(cls, value: str) -> str:
                            if not value.startswith('1.'):
                                raise ValueError(f'Invalid WBS number: {value}')
                            return value

                        class Config:
                            validate_assignment = True
                            extra = 'allow'

                    class Panels(CommonBaseModel):
                        wbs_no: Optional[str] = Field('1.2.2.2.2.7')

                        @field_validator('wbs_no')
                        def validate_wbs_no(cls, value: str) -> str:
                            if not value.startswith('1.'):
                                raise ValueError(f'Invalid WBS number: {value}')
                            return value

                        class Config:
                            validate_assignment = True
                            extra = 'allow'

                    class Misc(CommonBaseModel):
                        wbs_no: Optional[str] = Field('1.2.2.2.2.8')

                        @field_validator('wbs_no')
                        def validate_wbs_no(cls, value: str) -> str:
                            if not value.startswith('1.'):
                                raise ValueError(f'Invalid WBS number: {value}')
                            return value

                        class Config:
                            validate_assignment = True
                            extra = 'allow'

            class Wing(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.2.3')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

                class BasicStructure(CommonBaseModel):
                    wbs_no: Optional[str] = Field('1.2.2.3.1')

                    @field_validator('wbs_no')
                    def validate_wbs_no(cls, value: str) -> str:
                        if not value.startswith('1.'):
                            raise ValueError(f'Invalid WBS number: {value}')
                        return value

                    class Config:
                        validate_assignment = True
                        extra = 'allow'

                    class CenterSection(CommonBaseModel):
                        wbs_no: Optional[str] = Field('1.2.2.3.1.1')

                        @field_validator('wbs_no')
                        def validate_wbs_no(cls, value: str) -> str:
                            if not value.startswith('1.'):
                                raise ValueError(f'Invalid WBS number: {value}')
                            return value

                        class Config:
                            validate_assignment = True
                            extra = 'allow'

                        class Skins(CommonBaseModel):
                            wbs_no: Optional[str] = Field('1.2.2.3.1.1.1')

                            @field_validator('wbs_no')
                            def validate_wbs_no(cls, value: str) -> str:
                                if not value.startswith('1.'):
                                    raise ValueError(f'Invalid WBS number: {value}')
                                return value

                            class Config:
                                validate_assignment = True
                                extra = 'allow'

                        class Spars(CommonBaseModel):
                            wbs_no: Optional[str] = Field('1.2.2.3.1.1.2')

                            @field_validator('wbs_no')
                            def validate_wbs_no(cls, value: str) -> str:
                                if not value.startswith('1.'):
                                    raise ValueError(f'Invalid WBS number: {value}')
                                return value

                            class Config:
                                validate_assignment = True
                                extra = 'allow'

                        class Ribs(CommonBaseModel):
                            wbs_no: Optional[str] = Field('1.2.2.3.1.1.3')

                            @field_validator('wbs_no')
                            def validate_wbs_no(cls, value: str) -> str:
                                if not value.startswith('1.'):
                                    raise ValueError(f'Invalid WBS number: {value}')
                                return value

                            class Config:
                                validate_assignment = True
                                extra = 'allow'

                        class Stringers(CommonBaseModel):
                            wbs_no: Optional[str] = Field('1.2.2.3.1.1.4')

                            @field_validator('wbs_no')
                            def validate_wbs_no(cls, value: str) -> str:
                                if not value.startswith('1.'):
                                    raise ValueError(f'Invalid WBS number: {value}')
                                return value

                            class Config:
                                validate_assignment = True
                                extra = 'allow'

                        class Clips(CommonBaseModel):
                            wbs_no: Optional[str] = Field('1.2.2.3.1.1.5')

                            @field_validator('wbs_no')
                            def validate_wbs_no(cls, value: str) -> str:
                                if not value.startswith('1.'):
                                    raise ValueError(f'Invalid WBS number: {value}')
                                return value

                            class Config:
                                validate_assignment = True
                                extra = 'allow'

                    class IntermediatePanel(CommonBaseModel):
                        wbs_no: Optional[str] = Field('1.2.2.3.1.2')

                        @field_validator('wbs_no')
                        def validate_wbs_no(cls, value: str) -> str:
                            if not value.startswith('1.'):
                                raise ValueError(f'Invalid WBS number: {value}')
                            return value

                        class Config:
                            validate_assignment = True
                            extra = 'allow'

                        class Skins(CommonBaseModel):
                            wbs_no: Optional[str] = Field('1.2.2.3.1.2.1')

                            @field_validator('wbs_no')
                            def validate_wbs_no(cls, value: str) -> str:
                                if not value.startswith('1.'):
                                    raise ValueError(f'Invalid WBS number: {value}')
                                return value

                            class Config:
                                validate_assignment = True
                                extra = 'allow'

                        class Spars(CommonBaseModel):
                            wbs_no: Optional[str] = Field('1.2.2.3.1.2.2')

                            @field_validator('wbs_no')
                            def validate_wbs_no(cls, value: str) -> str:
                                if not value.startswith('1.'):
                                    raise ValueError(f'Invalid WBS number: {value}')
                                return value

                            class Config:
                                validate_assignment = True
                                extra = 'allow'

                        class Ribs(CommonBaseModel):
                            wbs_no: Optional[str] = Field('1.2.2.3.1.2.3')

                            @field_validator('wbs_no')
                            def validate_wbs_no(cls, value: str) -> str:
                                if not value.startswith('1.'):
                                    raise ValueError(f'Invalid WBS number: {value}')
                                return value

                            class Config:
                                validate_assignment = True
                                extra = 'allow'

                        class Stringers(CommonBaseModel):
                            wbs_no: Optional[str] = Field('1.2.2.3.1.2.4')

                            @field_validator('wbs_no')
                            def validate_wbs_no(cls, value: str) -> str:
                                if not value.startswith('1.'):
                                    raise ValueError(f'Invalid WBS number: {value}')
                                return value

                            class Config:
                                validate_assignment = True
                                extra = 'allow'

                        class Clips(CommonBaseModel):
                            wbs_no: Optional[str] = Field('1.2.2.3.1.2.5')

                            @field_validator('wbs_no')
                            def validate_wbs_no(cls, value: str) -> str:
                                if not value.startswith('1.'):
                                    raise ValueError(f'Invalid WBS number: {value}')
                                return value

                            class Config:
                                validate_assignment = True
                                extra = 'allow'

                    class OuterPanel(CommonBaseModel):
                        wbs_no: Optional[str] = Field('1.2.2.3.1.3')

                        @field_validator('wbs_no')
                        def validate_wbs_no(cls, value: str) -> str:
                            if not value.startswith('1.'):
                                raise ValueError(f'Invalid WBS number: {value}')
                            return value

                        class Config:
                            validate_assignment = True
                            extra = 'allow'

                        class Skins(CommonBaseModel):
                            wbs_no: Optional[str] = Field('1.2.2.3.1.3.1')

                            @field_validator('wbs_no')
                            def validate_wbs_no(cls, value: str) -> str:
                                if not value.startswith('1.'):
                                    raise ValueError(f'Invalid WBS number: {value}')
                                return value

                            class Config:
                                validate_assignment = True
                                extra = 'allow'

                        class Spars(CommonBaseModel):
                            wbs_no: Optional[str] = Field('1.2.2.3.1.3.2')

                            @field_validator('wbs_no')
                            def validate_wbs_no(cls, value: str) -> str:
                                if not value.startswith('1.'):
                                    raise ValueError(f'Invalid WBS number: {value}')
                                return value

                            class Config:
                                validate_assignment = True
                                extra = 'allow'

                        class Ribs(CommonBaseModel):
                            wbs_no: Optional[str] = Field('1.2.2.3.1.3.3')

                            @field_validator('wbs_no')
                            def validate_wbs_no(cls, value: str) -> str:
                                if not value.startswith('1.'):
                                    raise ValueError(f'Invalid WBS number: {value}')
                                return value

                            class Config:
                                validate_assignment = True
                                extra = 'allow'

                        class Stringers(CommonBaseModel):
                            wbs_no: Optional[str] = Field('1.2.2.3.1.3.4')

                            @field_validator('wbs_no')
                            def validate_wbs_no(cls, value: str) -> str:
                                if not value.startswith('1.'):
                                    raise ValueError(f'Invalid WBS number: {value}')
                                return value

                            class Config:
                                validate_assignment = True
                                extra = 'allow'

                        class Clips(CommonBaseModel):
                            wbs_no: Optional[str] = Field('1.2.2.3.1.3.5')

                            @field_validator('wbs_no')
                            def validate_wbs_no(cls, value: str) -> str:
                                if not value.startswith('1.'):
                                    raise ValueError(f'Invalid WBS number: {value}')
                                return value

                            class Config:
                                validate_assignment = True
                                extra = 'allow'

                class SecondaryStructure(CommonBaseModel):
                    wbs_no: Optional[str] = Field('1.2.2.3.2')

                    @field_validator('wbs_no')
                    def validate_wbs_no(cls, value: str) -> str:
                        if not value.startswith('1.'):
                            raise ValueError(f'Invalid WBS number: {value}')
                        return value

                    class Config:
                        validate_assignment = True
                        extra = 'allow'

                    class AccessPanels(CommonBaseModel):
                        wbs_no: Optional[str] = Field('1.2.2.3.2.1')

                        @field_validator('wbs_no')
                        def validate_wbs_no(cls, value: str) -> str:
                            if not value.startswith('1.'):
                                raise ValueError(f'Invalid WBS number: {value}')
                            return value

                        class Config:
                            validate_assignment = True
                            extra = 'allow'

                class Ailerons(CommonBaseModel):
                    wbs_no: Optional[str] = Field('1.2.2.3.3')

                    @field_validator('wbs_no')
                    def validate_wbs_no(cls, value: str) -> str:
                        if not value.startswith('1.'):
                            raise ValueError(f'Invalid WBS number: {value}')
                        return value

                    class Config:
                        validate_assignment = True
                        extra = 'allow'

                class Elevons(CommonBaseModel):
                    wbs_no: Optional[str] = Field('1.2.2.3.4')

                    @field_validator('wbs_no')
                    def validate_wbs_no(cls, value: str) -> str:
                        if not value.startswith('1.'):
                            raise ValueError(f'Invalid WBS number: {value}')
                        return value

                    class Config:
                        validate_assignment = True
                        extra = 'allow'

                class Spoilers(CommonBaseModel):
                    wbs_no: Optional[str] = Field('1.2.2.3.5')

                    @field_validator('wbs_no')
                    def validate_wbs_no(cls, value: str) -> str:
                        if not value.startswith('1.'):
                            raise ValueError(f'Invalid WBS number: {value}')
                        return value

                    class Config:
                        validate_assignment = True
                        extra = 'allow'

                class TrailingEdgeFlaps(CommonBaseModel):
                    wbs_no: Optional[str] = Field('1.2.2.3.6')

                    @field_validator('wbs_no')
                    def validate_wbs_no(cls, value: str) -> str:
                        if not value.startswith('1.'):
                            raise ValueError(f'Invalid WBS number: {value}')
                        return value

                    class Config:
                        validate_assignment = True
                        extra = 'allow'

                class LeadingEdgeFlaps(CommonBaseModel):
                    wbs_no: Optional[str] = Field('1.2.2.3.7')

                    @field_validator('wbs_no')
                    def validate_wbs_no(cls, value: str) -> str:
                        if not value.startswith('1.'):
                            raise ValueError(f'Invalid WBS number: {value}')
                        return value

                    class Config:
                        validate_assignment = True
                        extra = 'allow'

                class Slats(CommonBaseModel):
                    wbs_no: Optional[str] = Field('1.2.2.3.8')

                    @field_validator('wbs_no')
                    def validate_wbs_no(cls, value: str) -> str:
                        if not value.startswith('1.'):
                            raise ValueError(f'Invalid WBS number: {value}')
                        return value

                    class Config:
                        validate_assignment = True
                        extra = 'allow'

            class Empennage(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.2.4')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

                class Stabilizer(CommonBaseModel):
                    wbs_no: Optional[str] = Field('1.2.2.4.1')

                    @field_validator('wbs_no')
                    def validate_wbs_no(cls, value: str) -> str:
                        if not value.startswith('1.'):
                            raise ValueError(f'Invalid WBS number: {value}')
                        return value

                    class Config:
                        validate_assignment = True
                        extra = 'allow'

                    class BasicStructure(CommonBaseModel):
                        wbs_no: Optional[str] = Field('1.2.2.4.1.1')

                        @field_validator('wbs_no')
                        def validate_wbs_no(cls, value: str) -> str:
                            if not value.startswith('1.'):
                                raise ValueError(f'Invalid WBS number: {value}')
                            return value

                        class Config:
                            validate_assignment = True
                            extra = 'allow'

                        class CenterSection(CommonBaseModel):
                            wbs_no: Optional[str] = Field('1.2.2.4.1.1.1')

                            @field_validator('wbs_no')
                            def validate_wbs_no(cls, value: str) -> str:
                                if not value.startswith('1.'):
                                    raise ValueError(f'Invalid WBS number: {value}')
                                return value

                            class Config:
                                validate_assignment = True
                                extra = 'allow'

                            class Skins(CommonBaseModel):
                                wbs_no: Optional[str] = Field('1.2.2.4.1.1.1.1')

                                @field_validator('wbs_no')
                                def validate_wbs_no(cls, value: str) -> str:
                                    if not value.startswith('1.'):
                                        raise ValueError(f'Invalid WBS number: {value}')
                                    return value

                                class Config:
                                    validate_assignment = True
                                    extra = 'allow'

                            class Spars(CommonBaseModel):
                                wbs_no: Optional[str] = Field('1.2.2.4.1.1.1.2')

                                @field_validator('wbs_no')
                                def validate_wbs_no(cls, value: str) -> str:
                                    if not value.startswith('1.'):
                                        raise ValueError(f'Invalid WBS number: {value}')
                                    return value

                                class Config:
                                    validate_assignment = True
                                    extra = 'allow'

                            class Ribs(CommonBaseModel):
                                wbs_no: Optional[str] = Field('1.2.2.4.1.1.1.3')

                                @field_validator('wbs_no')
                                def validate_wbs_no(cls, value: str) -> str:
                                    if not value.startswith('1.'):
                                        raise ValueError(f'Invalid WBS number: {value}')
                                    return value

                                class Config:
                                    validate_assignment = True
                                    extra = 'allow'

                            class Stringers(CommonBaseModel):
                                wbs_no: Optional[str] = Field('1.2.2.4.1.1.1.4')

                                @field_validator('wbs_no')
                                def validate_wbs_no(cls, value: str) -> str:
                                    if not value.startswith('1.'):
                                        raise ValueError(f'Invalid WBS number: {value}')
                                    return value

                                class Config:
                                    validate_assignment = True
                                    extra = 'allow'

                            class Clips(CommonBaseModel):
                                wbs_no: Optional[str] = Field('1.2.2.4.1.1.1.5')

                                @field_validator('wbs_no')
                                def validate_wbs_no(cls, value: str) -> str:
                                    if not value.startswith('1.'):
                                        raise ValueError(f'Invalid WBS number: {value}')
                                    return value

                                class Config:
                                    validate_assignment = True
                                    extra = 'allow'

                        class IntermediatePanel(CommonBaseModel):
                            wbs_no: Optional[str] = Field('1.2.2.4.1.1.2')

                            @field_validator('wbs_no')
                            def validate_wbs_no(cls, value: str) -> str:
                                if not value.startswith('1.'):
                                    raise ValueError(f'Invalid WBS number: {value}')
                                return value

                            class Config:
                                validate_assignment = True
                                extra = 'allow'

                            class Skins(CommonBaseModel):
                                wbs_no: Optional[str] = Field('1.2.2.4.1.1.2.1')

                                @field_validator('wbs_no')
                                def validate_wbs_no(cls, value: str) -> str:
                                    if not value.startswith('1.'):
                                        raise ValueError(f'Invalid WBS number: {value}')
                                    return value

                                class Config:
                                    validate_assignment = True
                                    extra = 'allow'

                            class Spars(CommonBaseModel):
                                wbs_no: Optional[str] = Field('1.2.2.4.1.1.2.2')

                                @field_validator('wbs_no')
                                def validate_wbs_no(cls, value: str) -> str:
                                    if not value.startswith('1.'):
                                        raise ValueError(f'Invalid WBS number: {value}')
                                    return value

                                class Config:
                                    validate_assignment = True
                                    extra = 'allow'

                            class Ribs(CommonBaseModel):
                                wbs_no: Optional[str] = Field('1.2.2.4.1.1.2.3')

                                @field_validator('wbs_no')
                                def validate_wbs_no(cls, value: str) -> str:
                                    if not value.startswith('1.'):
                                        raise ValueError(f'Invalid WBS number: {value}')
                                    return value

                                class Config:
                                    validate_assignment = True
                                    extra = 'allow'

                            class Stringers(CommonBaseModel):
                                wbs_no: Optional[str] = Field('1.2.2.4.1.1.2.4')

                                @field_validator('wbs_no')
                                def validate_wbs_no(cls, value: str) -> str:
                                    if not value.startswith('1.'):
                                        raise ValueError(f'Invalid WBS number: {value}')
                                    return value

                                class Config:
                                    validate_assignment = True
                                    extra = 'allow'

                            class Clips(CommonBaseModel):
                                wbs_no: Optional[str] = Field('1.2.2.4.1.1.2.5')

                                @field_validator('wbs_no')
                                def validate_wbs_no(cls, value: str) -> str:
                                    if not value.startswith('1.'):
                                        raise ValueError(f'Invalid WBS number: {value}')
                                    return value

                                class Config:
                                    validate_assignment = True
                                    extra = 'allow'

                        class OuterPanel(CommonBaseModel):
                            wbs_no: Optional[str] = Field('1.2.2.4.1.1.3')

                            @field_validator('wbs_no')
                            def validate_wbs_no(cls, value: str) -> str:
                                if not value.startswith('1.'):
                                    raise ValueError(f'Invalid WBS number: {value}')
                                return value

                            class Config:
                                validate_assignment = True
                                extra = 'allow'

                            class Skins(CommonBaseModel):
                                wbs_no: Optional[str] = Field('1.2.2.4.1.1.3.1')

                                @field_validator('wbs_no')
                                def validate_wbs_no(cls, value: str) -> str:
                                    if not value.startswith('1.'):
                                        raise ValueError(f'Invalid WBS number: {value}')
                                    return value

                                class Config:
                                    validate_assignment = True
                                    extra = 'allow'

                            class Spars(CommonBaseModel):
                                wbs_no: Optional[str] = Field('1.2.2.4.1.1.3.2')

                                @field_validator('wbs_no')
                                def validate_wbs_no(cls, value: str) -> str:
                                    if not value.startswith('1.'):
                                        raise ValueError(f'Invalid WBS number: {value}')
                                    return value

                                class Config:
                                    validate_assignment = True
                                    extra = 'allow'

                            class Ribs(CommonBaseModel):
                                wbs_no: Optional[str] = Field('1.2.2.4.1.1.3.3')

                                @field_validator('wbs_no')
                                def validate_wbs_no(cls, value: str) -> str:
                                    if not value.startswith('1.'):
                                        raise ValueError(f'Invalid WBS number: {value}')
                                    return value

                                class Config:
                                    validate_assignment = True
                                    extra = 'allow'

                            class Stringers(CommonBaseModel):
                                wbs_no: Optional[str] = Field('1.2.2.4.1.1.3.4')

                                @field_validator('wbs_no')
                                def validate_wbs_no(cls, value: str) -> str:
                                    if not value.startswith('1.'):
                                        raise ValueError(f'Invalid WBS number: {value}')
                                    return value

                                class Config:
                                    validate_assignment = True
                                    extra = 'allow'

                            class Clips(CommonBaseModel):
                                wbs_no: Optional[str] = Field('1.2.2.4.1.1.3.5')

                                @field_validator('wbs_no')
                                def validate_wbs_no(cls, value: str) -> str:
                                    if not value.startswith('1.'):
                                        raise ValueError(f'Invalid WBS number: {value}')
                                    return value

                                class Config:
                                    validate_assignment = True
                                    extra = 'allow'

                    class SecondaryStructure(CommonBaseModel):
                        wbs_no: Optional[str] = Field('1.2.2.4.2')

                        @field_validator('wbs_no')
                        def validate_wbs_no(cls, value: str) -> str:
                            if not value.startswith('1.'):
                                raise ValueError(f'Invalid WBS number: {value}')
                            return value

                        class Config:
                            validate_assignment = True
                            extra = 'allow'

                        class AccessPanels(CommonBaseModel):
                            wbs_no: Optional[str] = Field('1.2.2.4.2.1')

                            @field_validator('wbs_no')
                            def validate_wbs_no(cls, value: str) -> str:
                                if not value.startswith('1.'):
                                    raise ValueError(f'Invalid WBS number: {value}')
                                return value

                            class Config:
                                validate_assignment = True
                                extra = 'allow'

                class Ailerons(CommonBaseModel):
                    wbs_no: Optional[str] = Field('1.2.2.4.3')

                    @field_validator('wbs_no')
                    def validate_wbs_no(cls, value: str) -> str:
                        if not value.startswith('1.'):
                            raise ValueError(f'Invalid WBS number: {value}')
                        return value

                    class Config:
                        validate_assignment = True
                        extra = 'allow'

                class Elevons(CommonBaseModel):
                    wbs_no: Optional[str] = Field('1.2.2.4.4')

                    @field_validator('wbs_no')
                    def validate_wbs_no(cls, value: str) -> str:
                        if not value.startswith('1.'):
                            raise ValueError(f'Invalid WBS number: {value}')
                        return value

                    class Config:
                        validate_assignment = True
                        extra = 'allow'

                class Spoilers(CommonBaseModel):
                    wbs_no: Optional[str] = Field('1.2.2.4.5')

                    @field_validator('wbs_no')
                    def validate_wbs_no(cls, value: str) -> str:

                        if not value.startswith('1.'):
                            raise ValueError(f'Invalid WBS number: {value}')
                        return value

                    class Config:
                        validate_assignment = True
                        extra = 'allow'

                class TrailingEdgeFlaps(CommonBaseModel):
                    wbs_no: Optional[str] = Field('1.2.2.4.6')

                    @field_validator('wbs_no')
                    def validate_wbs_no(cls, value: str) -> str:
                        if not value.startswith('1.'):
                            raise ValueError(f'Invalid WBS number: {value}')
                        return value

                    class Config:
                        validate_assignment = True
                        extra = 'allow'

                class LeadingEdgeFlaps(CommonBaseModel):
                    wbs_no: Optional[str] = Field('1.2.2.4.7')

                    @field_validator('wbs_no')
                    def validate_wbs_no(cls, value: str) -> str:
                        if not value.startswith('1.'):
                            raise ValueError(f'Invalid WBS number: {value}')
                        return value

                    class Config:
                        validate_assignment = True
                        extra = 'allow'

                class Slats(CommonBaseModel):
                    wbs_no: Optional[str] = Field('1.2.2.4.8')

                    @field_validator('wbs_no')
                    def validate_wbs_no(cls, value: str) -> str:
                        if not value.startswith('1.'):
                            raise ValueError(f'Invalid WBS number: {value}')
                        return value

                    class Config:
                        validate_assignment = True
                        extra = 'allow'

            class Nacelle(Component):
                wbs_no: Optional[str] = Field('1.2.2.5')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

                class BasicStructure(CommonBaseModel):
                    wbs_no: Optional[str] = Field('1.2.2.5.1')

                    @field_validator('wbs_no')
                    def validate_wbs_no(cls, value: str) -> str:
                        if not value.startswith('1.'):
                            raise ValueError(f'Invalid WBS number: {value}')
                        return value

                    class Config:
                        validate_assignment = True
                        extra = 'allow'

                    class Skins(CommonBaseModel):
                        wbs_no: Optional[str] = Field('1.2.2.5.1.1')

                        @field_validator('wbs_no')
                        def validate_wbs_no(cls, value: str) -> str:
                            if not value.startswith('1.'):
                                raise ValueError(f'Invalid WBS number: {value}')
                            return value

                        class Config:
                            validate_assignment = True
                            extra = 'allow'

                    class Stringers(CommonBaseModel):
                        wbs_no: Optional[str] = Field('1.2.2.5.1.2')

                        @field_validator('wbs_no')
                        def validate_wbs_no(cls, value: str) -> str:
                            if not value.startswith('1.'):
                                raise ValueError(f'Invalid WBS number: {value}')
                            return value

                        class Config:
                            validate_assignment = True
                            extra = 'allow'

                    class Frames(CommonBaseModel):
                        wbs_no: Optional[str] = Field('1.2.2.5.1.3')

                        @field_validator('wbs_no')
                        def validate_wbs_no(cls, value: str) -> str:
                            if not value.startswith('1.'):
                                raise ValueError(f'Invalid WBS number: {value}')
                            return value

                        class Config:
                            validate_assignment = True
                            extra = 'allow'

                    class Clips(CommonBaseModel):
                        wbs_no: Optional[str] = Field('1.2.2.5.1.4')

                        @field_validator('wbs_no')
                        def validate_wbs_no(cls, value: str) -> str:
                            if not value.startswith('1.'):
                                raise ValueError(f'Invalid WBS number: {value}')
                            return value

                        class Config:
                            validate_assignment = True
                            extra = 'allow'

                    class Beams(CommonBaseModel):
                        wbs_no: Optional[str] = Field('1.2.2.5.1.5')

                        @field_validator('wbs_no')
                        def validate_wbs_no(cls, value: str) -> str:
                            if not value.startswith('1.'):
                                raise ValueError(f'Invalid WBS number: {value}')
                            return value

                        class Config:
                            validate_assignment = True
                            extra = 'allow'

                    class Floors(CommonBaseModel):
                        wbs_no: Optional[str] = Field('1.2.2.5.1.6')

                        @field_validator('wbs_no')
                        def validate_wbs_no(cls, value: str) -> str:
                            if not value.startswith('1.'):
                                raise ValueError(f'Invalid WBS number: {value}')
                            return value

                        class Config:
                            validate_assignment = True
                            extra = 'allow'

                    class Bulkheads(CommonBaseModel):
                        wbs_no: Optional[str] = Field('1.2.2.5.1.7')

                        @field_validator('wbs_no')
                        def validate_wbs_no(cls, value: str) -> str:
                            if not value.startswith('1.'):
                                raise ValueError(f'Invalid WBS number: {value}')
                            return value

                        class Config:
                            validate_assignment = True
                            extra = 'allow'

                    class Longerons(CommonBaseModel):
                        wbs_no: Optional[str] = Field('1.2.2.5.1.8')

                        @field_validator('wbs_no')
                        def validate_wbs_no(cls, value: str) -> str:
                            if not value.startswith('1.'):
                                raise ValueError(f'Invalid WBS number: {value}')
                            return value

                        class Config:
                            validate_assignment = True
                            extra = 'allow'

                    class Supports(CommonBaseModel):
                        wbs_no: Optional[str] = Field('1.2.2.5.1.9')

                        @field_validator('wbs_no')
                        def validate_wbs_no(cls, value: str) -> str:
                            if not value.startswith('1.'):
                                raise ValueError(f'Invalid WBS number: {value}')
                            return value

                        class Config:
                            validate_assignment = True
                            extra = 'allow'

                class SecondaryStructure(CommonBaseModel):
                    wbs_no: Optional[str] = Field('1.2.2.5.2')

                    @field_validator('wbs_no')
                    def validate_wbs_no(cls, value: str) -> str:
                        if not value.startswith('1.'):
                            raise ValueError(f'Invalid WBS number: {value}')
                        return value

                    class Config:
                        validate_assignment = True
                        extra = 'allow'

                    class Enclosures(CommonBaseModel):
                        wbs_no: Optional[str] = Field('1.2.2.5.2.1')

                        @field_validator('wbs_no')
                        def validate_wbs_no(cls, value: str) -> str:
                            if not value.startswith('1.'):
                                raise ValueError(f'Invalid WBS number: {value}')
                            return value

                        class Config:
                            validate_assignment = True
                            extra = 'allow'

                    class Flooring(CommonBaseModel):
                        wbs_no: Optional[str] = Field('1.2.2.5.2.2')

                        @field_validator('wbs_no')
                        def validate_wbs_no(cls, value: str) -> str:
                            if not value.startswith('1.'):
                                raise ValueError(f'Invalid WBS number: {value}')
                            return value

                        class Config:
                            validate_assignment = True
                            extra = 'allow'

                    class Partitions(CommonBaseModel):
                        wbs_no: Optional[str] = Field('1.2.2.5.2.3')

                        @field_validator('wbs_no')
                        def validate_wbs_no(cls, value: str) -> str:
                            if not value.startswith('1.'):
                                raise ValueError(f'Invalid WBS number: {value}')
                            return value

                        class Config:
                            validate_assignment = True
                            extra = 'allow'

                    class Windows(CommonBaseModel):
                        wbs_no: Optional[str] = Field('1.2.2.5.2.4')

                        @field_validator('wbs_no')
                        def validate_wbs_no(cls, value: str) -> str:
                            if not value.startswith('1.'):
                                raise ValueError(f'Invalid WBS number: {value}')
                            return value

                        class Config:
                            validate_assignment = True
                            extra = 'allow'

                    class Doors(CommonBaseModel):
                        wbs_no: Optional[str] = Field('1.2.2.5.2.5')

                        @field_validator('wbs_no')
                        def validate_wbs_no(cls, value: str) -> str:
                            if not value.startswith('1.'):
                                raise ValueError(f'Invalid WBS number: {value}')
                            return value

                        class Config:
                            validate_assignment = True
                            extra = 'allow'

                    class Ramps(CommonBaseModel):
                        wbs_no: Optional[str] = Field('1.2.2.5.2.6')

                        @field_validator('wbs_no')
                        def validate_wbs_no(cls, value: str) -> str:
                            if not value.startswith('1.'):
                                raise ValueError(f'Invalid WBS number: {value}')
                            return value

                        class Config:
                            validate_assignment = True
                            extra = 'allow'

                    class Panels(CommonBaseModel):
                        wbs_no: Optional[str] = Field('1.2.2.5.2.7')

                        @field_validator('wbs_no')
                        def validate_wbs_no(cls, value: str) -> str:
                            if not value.startswith('1.'):
                                raise ValueError(f'Invalid WBS number: {value}')
                            return value

                        class Config:
                            validate_assignment = True
                            extra = 'allow'

                    class Misc(CommonBaseModel):
                        wbs_no: Optional[str] = Field('1.2.2.5.2.8')

                        @field_validator('wbs_no')
                        def validate_wbs_no(cls, value: str) -> str:
                            if not value.startswith('1.'):
                                raise ValueError(f'Invalid WBS number: {value}')
                            return value

                        class Config:
                            validate_assignment = True
                            extra = 'allow'

        class Propulsion(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.2.3')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

            class Engine(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.3.1')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class EngineInstallation(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.3.2')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class AccessoryGearBoxesAndDrive(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.3.3')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class ExhaustSystem(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.3.4')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class EngineCooling(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.3.5')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class WaterInjection(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.3.6')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class EngineControls(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.3.7')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class StartingSystem(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.3.8')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class PropellerOrFanInstallation(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.3.9')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class LubricatingSystem(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.3.10')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class FuelSystem(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.3.11')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

                class ProtectedTanks(CommonBaseModel):
                    wbs_no: Optional[str] = Field('1.2.3.11.1')

                    @field_validator('wbs_no')
                    def validate_wbs_no(cls, value: str) -> str:
                        if not value.startswith('1.'):
                            raise ValueError(f'Invalid WBS number: {value}')
                        return value

                    class Config:
                        validate_assignment = True
                        extra = 'allow'

                class UnprotectedTanks(CommonBaseModel):
                    wbs_no: Optional[str] = Field('1.2.3.11.2')

                    @field_validator('wbs_no')
                    def validate_wbs_no(cls, value: str) -> str:
                        if not value.startswith('1.'):
                            raise ValueError(f'Invalid WBS number: {value}')
                        return value

                    class Config:
                        validate_assignment = True
                        extra = 'allow'

                class Plumbing(CommonBaseModel):
                    wbs_no: Optional[str] = Field('1.2.3.11.3')

                    @field_validator('wbs_no')
                    def validate_wbs_no(cls, value: str) -> str:
                        if not value.startswith('1.'):
                            raise ValueError(f'Invalid WBS number: {value}')
                        return value

                    class Config:
                        validate_assignment = True
                        extra = 'allow'

                class Etc(CommonBaseModel):
                    wbs_no: Optional[str] = Field('1.2.3.11.4')

                    @field_validator('wbs_no')
                    def validate_wbs_no(cls, value: str) -> str:
                        if not value.startswith('1.'):
                            raise ValueError(f'Invalid WBS number: {value}')
                        return value

                    class Config:
                        validate_assignment = True
                        extra = 'allow'

            class DriveSystem(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.3.12')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

                class GearBoxes(CommonBaseModel):
                    wbs_no: Optional[str] = Field('1.2.3.12.1')

                    @field_validator('wbs_no')
                    def validate_wbs_no(cls, value: str) -> str:
                        if not value.startswith('1.'):
                            raise ValueError(f'Invalid WBS number: {value}')
                        return value

                    class Config:
                        validate_assignment = True
                        extra = 'allow'

                class LubSys(CommonBaseModel):
                    wbs_no: Optional[str] = Field('1.2.3.12.2')

                    @field_validator('wbs_no')
                    def validate_wbs_no(cls, value: str) -> str:
                        if not value.startswith('1.'):
                            raise ValueError(f'Invalid WBS number: {value}')
                        return value

                    class Config:
                        validate_assignment = True
                        extra = 'allow'

                class RtrBrk(CommonBaseModel):
                    wbs_no: Optional[str] = Field('1.2.3.12.3')

                    @field_validator('wbs_no')
                    def validate_wbs_no(cls, value: str) -> str:
                        if not value.startswith('1.'):
                            raise ValueError(f'Invalid WBS number: {value}')
                        return value

                    class Config:
                        validate_assignment = True
                        extra = 'allow'

                class TransmissionDrive(CommonBaseModel):
                    wbs_no: Optional[str] = Field('1.2.3.12.4')

                    @field_validator('wbs_no')
                    def validate_wbs_no(cls, value: str) -> str:
                        if not value.startswith('1.'):
                            raise ValueError(f'Invalid WBS number: {value}')
                        return value

                    class Config:
                        validate_assignment = True
                        extra = 'allow'

                class RotorShaft(CommonBaseModel):
                    wbs_no: Optional[str] = Field('1.2.3.12.5')

                    @field_validator('wbs_no')
                    def validate_wbs_no(cls, value: str) -> str:
                        if not value.startswith('1.'):
                            raise ValueError(f'Invalid WBS number: {value}')
                        return value

                    class Config:
                        validate_assignment = True
                        extra = 'allow'

                class GasDrive(CommonBaseModel):
                    wbs_no: Optional[str] = Field('1.2.3.12.6')

                    @field_validator('wbs_no')
                    def validate_wbs_no(cls, value: str) -> str:
                        if not value.startswith('1.'):
                            raise ValueError(f'Invalid WBS number: {value}')
                        return value

                    class Config:
                        validate_assignment = True
                        extra = 'allow'

        class VehicleSubsystems(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.2.4')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

            class VehicleSubsystemIntegrationAssemblyTestAndCheckout(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.4.1')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class FlightControlSubsystem(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.4.2')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

                class CockpitControls(CommonBaseModel):
                    wbs_no: Optional[str] = Field('1.2.4.2.1')

                    @field_validator('wbs_no')
                    def validate_wbs_no(cls, value: str) -> str:
                        if not value.startswith('1.'):
                            raise ValueError(f'Invalid WBS number: {value}')
                        return value

                    class Config:
                        validate_assignment = True
                        extra = 'allow'

                class AutomaticFlightControlSystem(CommonBaseModel):
                    wbs_no: Optional[str] = Field('1.2.4.2.2')

                    @field_validator('wbs_no')
                    def validate_wbs_no(cls, value: str) -> str:
                        if not value.startswith('1.'):
                            raise ValueError(f'Invalid WBS number: {value}')
                        return value

                    class Config:
                        validate_assignment = True
                        extra = 'allow'

                class SystemControls(CommonBaseModel):
                    wbs_no: Optional[str] = Field('1.2.4.2.3')

                    @field_validator('wbs_no')
                    def validate_wbs_no(cls, value: str) -> str:
                        if not value.startswith('1.'):
                            raise ValueError(f'Invalid WBS number: {value}')
                        return value

                    class Config:
                        validate_assignment = True
                        extra = 'allow'

            class AuxiliaryPowerSubsystem(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.4.3')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class HydraulicSubsystem(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.4.4')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class ElectricalAntiIcingSystem(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.4.5')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class CrewStationSubsystem(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.4.6')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class EnvironmentalControlSubsystem(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.4.7')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class FuelSubsystem(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.4.8')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class Instruments(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.4.9')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class PneumaticSubsystem(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.4.10')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class AntiIcingSubsystem(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.4.11')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class VehicleSubsystemSoftware(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.4.12')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class OtherSubsystems(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.4.13')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

        class Avionics(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.2.5')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

            class AvionicsIntegrationAssemblyTestAndCheckout(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.5.1')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class CommunicationIdentification(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.5.2')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class NavigationGuidance(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.5.3')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class MissionComputerProcessing(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.5.4')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class FireControl(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.5.5')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class DataDisplayAndControls(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.5.6')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class Survivability(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.5.7')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class Reconnaissance(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.5.8')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class ElectronicWarfare(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.5.9')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class AutomaticFlightControl(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.5.10')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class HealthMonitoringSystem(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.5.11')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class StoresManagement(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.5.12')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class AvionicsSoftwareRelease(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.5.13')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class OtherAvionicsSubsystems(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.5.14')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class Installation(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.5.15')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

        class ArmamentWeaponsDelivery(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.2.6')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

        class AuxiliaryEquipment(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.2.7')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

        class FurnishingsAndEquipment(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.2.8')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

            class AccommodationForPersonnel(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.8.1')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class MiscellaneousEquipment(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.8.2')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class Furnishings(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.8.3')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class EmergencyEquipment(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.8.4')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

        class AirVehicleSoftwareRelease(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.2.9')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

        class LoadAndHandlingSystem(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.2.10')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

            class AircraftHandling(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.10.1')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class LoadHandling(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.10.2')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

        class BallastGroup(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.2.11')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

        class ManufacturingVariation(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.2.12')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

        class Contingency(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.2.13')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

        class OperatingItems(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.2.14')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

            class Crew(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.14.1')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class UnusableFuel(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.14.2')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class TrappedOil(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.14.3')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class EngineOil(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.14.4')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class AuxFuelTanks(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.14.5')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class InternalFuelTanks(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.14.6')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class ExternalFuelTanks(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.14.7')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class WaterInjectionFluid(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.14.8')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class Baggage(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.14.9')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class GunInstallations(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.14.10')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

                class Guns(CommonBaseModel):
                    wbs_no: Optional[str] = Field('1.2.14.10.1')

                    @field_validator('wbs_no')
                    def validate_wbs_no(cls, value: str) -> str:
                        if not value.startswith('1.'):
                            raise ValueError(f'Invalid WBS number: {value}')
                        return value

                    class Config:
                        validate_assignment = True
                        extra = 'allow'

                class Supports(CommonBaseModel):
                    wbs_no: Optional[str] = Field('1.2.14.10.2')

                    @field_validator('wbs_no')
                    def validate_wbs_no(cls, value: str) -> str:
                        if not value.startswith('1.'):
                            raise ValueError(f'Invalid WBS number: {value}')
                        return value

                    class Config:
                        validate_assignment = True
                        extra = 'allow'

            class WeaponsProvisions(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.14.11')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class Chaff(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.14.12')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class Flares(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.14.13')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class SurvivalKits(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.14.14')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class LifeRafts(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.14.15')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class Oxygen(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.2.14.16')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

        class Passengers(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.2.15')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

        class Troops(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.2.16')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

        class Cargo(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.2.17')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

        class Ammunition(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.2.18')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

        class Weapons(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.2.19')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

        class InternalUsableFuel(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.2.20')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

        class ExternalUsableFuel(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.2.21')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

        class OtherAirVehicle(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.2.22')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

    class PayloadMissionSystem(CommonBaseModel):
        wbs_no: Optional[str] = Field('1.3')

        @field_validator('wbs_no')
        def validate_wbs_no(cls, value: str) -> str:
            if not value.startswith('1.'):
                raise ValueError(f'Invalid WBS number: {value}')
            return value

        class Config:
            validate_assignment = True
            extra = 'allow'

        class PayloadIntegrationAssemblyTestAndCheckout(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.3.1')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

        class SurvivabilityPayload(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.3.2')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

        class ReconnaissancePayload(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.3.3')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

        class ElectronicWarfarePayload(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.3.4')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

        class ArmamentWeaponsDeliveryPayload(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.3.5')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

        class PayloadSoftwareRelease(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.3.6')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

        class OtherPayload(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.3.7')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

    class GroundHostSegment(CommonBaseModel):
        wbs_no: Optional[str] = Field('1.4')

        @field_validator('wbs_no')
        def validate_wbs_no(cls, value: str) -> str:
            if not value.startswith('1.'):
                raise ValueError(f'Invalid WBS number: {value}')
            return value

        class Config:
            validate_assignment = True
            extra = 'allow'

        class GroundSegmentIntegrationAssemblyTestAndCheckout(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.4.1')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

        class GroundControlSystems(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.4.2')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

        class CommandAndControlSubsystem(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.4.3')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

        class LaunchEquipment(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.4.4')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

        class RecoveryEquipment(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.4.5')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

        class TransportVehicles(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.4.6')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

        class GroundSegmentSoftwareRelease(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.4.7')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

        class OtherGroundHostSegment(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.4.8')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

    class AircraftSystemSoftwareRelease(CommonBaseModel):
        wbs_no: Optional[str] = Field('1.5')

        @field_validator('wbs_no')
        def validate_wbs_no(cls, value: str) -> str:
            if not value.startswith('1.'):
                raise ValueError(f'Invalid WBS number: {value}')
            return value

        class Config:
            validate_assignment = True
            extra = 'allow'

    class SystemsEngineering(CommonBaseModel):
        wbs_no: Optional[str] = Field('1.6')

        @field_validator('wbs_no')
        def validate_wbs_no(cls, value: str) -> str:
            if not value.startswith('1.'):
                raise ValueError(f'Invalid WBS number: {value}')
            return value

        class Config:
            validate_assignment = True
            extra = 'allow'

        class SoftwareSystemsEngineering(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.6.1')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

        class IntegratedLogisticsSupportSystemsEngineering(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.6.2')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

        class CybersecuritySystemsEngineering(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.6.3')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

        class CoreSystemsEngineering(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.6.4')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

        class OtherSystemsEngineering(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.6.5')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

    class ProgramManagement(CommonBaseModel):
        wbs_no: Optional[str] = Field('1.7')

        @field_validator('wbs_no')
        def validate_wbs_no(cls, value: str) -> str:
            if not value.startswith('1.'):
                raise ValueError(f'Invalid WBS number: {value}')
            return value

        class Config:
            validate_assignment = True
            extra = 'allow'

        class SoftwareProgramManagement(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.7.1')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

        class IntegratedLogisticsSupportProgramManagement(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.7.2')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

        class CybersecurityManagement(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.7.3')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

        class CoreProgramManagement(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.7.4')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

        class OtherProgramManagement(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.7.5')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

    class SystemTestAndEvaluation(CommonBaseModel):
        wbs_no: Optional[str] = Field('1.8')

        @field_validator('wbs_no')
        def validate_wbs_no(cls, value: str) -> str:
            if not value.startswith('1.'):
                raise ValueError(f'Invalid WBS number: {value}')
            return value

        class Config:
            validate_assignment = True
            extra = 'allow'

        class DevelopmentalTestAndEvaluation(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.8.1')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

            class SystemAcceptanceTest(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.8.1.1')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class WindTunnelTests(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.8.1.2')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class StructuralTests(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.8.1.3')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class FlightTests(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.8.1.4')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class GroundTests(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.8.1.5')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class CybersecurityTestAndEvaluation(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.8.1.6')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class OtherDTEtests(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.8.1.7')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

        class OperationalTestAndEvaluation(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.8.2')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

            class LimitedUserEvaluation(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.8.2.1')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class InteroperabilityTesting(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.8.2.2')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class FlightTests(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.8.2.3')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class GroundTests(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.8.2.4')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class CybersecurityTestAndEvaluation(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.8.2.5')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class OtherOTEtests(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.8.2.6')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

        class LiveFireTestAndEvaluation(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.8.3')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

        class MockupsSystemIntegrationLabs(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.8.4')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

        class TestAndEvaluationSupport(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.8.5')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

        class TestFacilities(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.8.6')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

    class Training(CommonBaseModel):
        wbs_no: Optional[str] = Field('1.9')

        @field_validator('wbs_no')
        def validate_wbs_no(cls, value: str) -> str:
            if not value.startswith('1.'):
                raise ValueError(f'Invalid WBS number: {value}')
            return value

        class Config:
            validate_assignment = True
            extra = 'allow'

        class Equipment(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.9.1')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

            class OperatorInstructionalEquipment(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.9.1.1')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class MaintainerInstructionalEquipment(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.9.1.2')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

        class Services(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.9.2')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

            class OperatorInstructionalServices(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.9.2.1')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class MaintainerInstructionalServices(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.9.2.2')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

        class Facilities(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.9.3')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

        class TrainingSoftware(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.9.4')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

    class Data(CommonBaseModel):
        wbs_no: Optional[str] = Field('1.10')

        @field_validator('wbs_no')
        def validate_wbs_no(cls, value: str) -> str:
            if not value.startswith('1.'):
                raise ValueError(f'Invalid WBS number: {value}')
            return value

        class Config:
            validate_assignment = True
            extra = 'allow'

        class DataDeliverables(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.10.1')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

        class DataRepository(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.10.2')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

        class DataRights(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.10.3')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

    class PeculiarSupportEquipment(CommonBaseModel):
        wbs_no: Optional[str] = Field('1.11')

        @field_validator('wbs_no')
        def validate_wbs_no(cls, value: str) -> str:
            if not value.startswith('1.'):
                raise ValueError(f'Invalid WBS number: {value}')
            return value

        class Config:
            validate_assignment = True
            extra = 'allow'

        class TestAndMeasurementEquipment(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.11.1')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

            class AirframeHullVehicle(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.11.1.1')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class Propulsion(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.11.1.2')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class ElectronicsAvionics(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.11.1.3')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class OtherMajorSubsystems(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.11.1.4')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

        class SupportAndHandlingEquipment(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.11.2')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

            class AirframeHullVehicle(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.11.2.1')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class Propulsion(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.11.2.2')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class ElectronicsAvionics(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.11.2.3')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class OtherMajorSubsystems(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.11.2.4')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

    class CommonSupportEquipment(CommonBaseModel):
        wbs_no: Optional[str] = Field('1.12')

        @field_validator('wbs_no')
        def validate_wbs_no(cls, value: str) -> str:
            if not value.startswith('1.'):
                raise ValueError(f'Invalid WBS number: {value}')
            return value

        class Config:
            validate_assignment = True
            extra = 'allow'

        class TestAndMeasurementEquipment(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.12.1')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

            class AirframeHullVehicle(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.12.1.1')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class Propulsion(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.12.1.2')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class ElectronicsAvionics(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.12.1.3')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class OtherMajorSubsystems(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.12.1.4')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

        class SupportAndHandlingEquipment(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.12.2')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

            class AirframeHullVehicle(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.12.2.1')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class Propulsion(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.12.2.2')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class ElectronicsAvionics(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.12.2.3')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

            class OtherMajorSubsystems(CommonBaseModel):
                wbs_no: Optional[str] = Field('1.12.2.4')

                @field_validator('wbs_no')
                def validate_wbs_no(cls, value: str) -> str:
                    if not value.startswith('1.'):
                        raise ValueError(f'Invalid WBS number: {value}')
                    return value

                class Config:
                    validate_assignment = True
                    extra = 'allow'

    class OperationalSiteActivation(CommonBaseModel):
        wbs_no: Optional[str] = Field('1.13')

        @field_validator('wbs_no')
        def validate_wbs_no(cls, value: str) -> str:
            if not value.startswith('1.'):
                raise ValueError(f'Invalid WBS number: {value}')
            return value

        class Config:
            validate_assignment = True
            extra = 'allow'

        class SystemAssemblyInstallationAndCheckoutOnSite(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.13.1')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

        class ContractorTechnicalSupport(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.13.2')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

        class SiteConstruction(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.13.3')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

        class SiteShipVehicleConversion(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.13.4')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

        class InterimContractorSupport(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.13.5')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

    class ContractorLogisticsSupport(CommonBaseModel):
        wbs_no: Optional[str] = Field('1.14')

        @field_validator('wbs_no')
        def validate_wbs_no(cls, value: str) -> str:
            if not value.startswith('1.'):
                raise ValueError(f'Invalid WBS number: {value}')
            return value

        class Config:
            validate_assignment = True
            extra = 'allow'

    class IndustrialFacilities(CommonBaseModel):
        wbs_no: Optional[str] = Field('1.15')

        @field_validator('wbs_no')
        def validate_wbs_no(cls, value: str) -> str:
            if not value.startswith('1.'):
                raise ValueError(f'Invalid WBS number: {value}')
            return value

        class Config:
            validate_assignment = True
            extra = 'allow'

        class ConstructionConversionExpansion(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.15.1')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

        class EquipmentAcquisitionOrModernization(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.15.2')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

        class IndustrialFacilitiesMaintenance(CommonBaseModel):
            wbs_no: Optional[str] = Field('1.15.3')

            @field_validator('wbs_no')
            def validate_wbs_no(cls, value: str) -> str:
                if not value.startswith('1.'):
                    raise ValueError(f'Invalid WBS number: {value}')
                return value

            class Config:
                validate_assignment = True
                extra = 'allow'

    class InitialSparesAndRepairParts(CommonBaseModel):
        wbs_no: Optional[str] = Field('1.16')

        @field_validator('wbs_no')
        def validate_wbs_no(cls, value: str) -> str:
            if not value.startswith('1.'):
                raise ValueError(f'Invalid WBS number: {value}')
            return value

        class Config:
            validate_assignment = True
            extra = 'allow'
