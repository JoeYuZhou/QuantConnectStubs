# encoding: utf-8
# module QuantConnect.Algorithm calls itself Algorithm
# from QuantConnect.Algorithm, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes
from QuantConnect.Data.UniverseSelection import UniverseSettings
class CandlestickPatterns(object):
    """
    Provides helpers for using candlestick patterns

    

    CandlestickPatterns(algorithm: QCAlgorithm)
    """
    def AbandonedBaby(self, symbol, penetration, resolution, selector):
        """ AbandonedBaby(self: CandlestickPatterns, symbol: Symbol, penetration: Decimal, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> AbandonedBaby """
        pass

    def AdvanceBlock(self, symbol, resolution, selector):
        """ AdvanceBlock(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> AdvanceBlock """
        pass

    def BeltHold(self, symbol, resolution, selector):
        """ BeltHold(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> BeltHold """
        pass

    def Breakaway(self, symbol, resolution, selector):
        """ Breakaway(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> Breakaway """
        pass

    def ClosingMarubozu(self, symbol, resolution, selector):
        """ ClosingMarubozu(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> ClosingMarubozu """
        pass

    def ConcealedBabySwallow(self, symbol, resolution, selector):
        """ ConcealedBabySwallow(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> ConcealedBabySwallow """
        pass

    def Counterattack(self, symbol, resolution, selector):
        """ Counterattack(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> Counterattack """
        pass

    def DarkCloudCover(self, symbol, penetration, resolution, selector):
        """ DarkCloudCover(self: CandlestickPatterns, symbol: Symbol, penetration: Decimal, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> DarkCloudCover """
        pass

    def Doji(self, symbol, resolution, selector):
        """ Doji(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> Doji """
        pass

    def DojiStar(self, symbol, resolution, selector):
        """ DojiStar(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> DojiStar """
        pass

    def DragonflyDoji(self, symbol, resolution, selector):
        """ DragonflyDoji(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> DragonflyDoji """
        pass

    def Engulfing(self, symbol, resolution, selector):
        """ Engulfing(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> Engulfing """
        pass

    def EveningDojiStar(self, symbol, penetration, resolution, selector):
        """ EveningDojiStar(self: CandlestickPatterns, symbol: Symbol, penetration: Decimal, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> EveningDojiStar """
        pass

    def EveningStar(self, symbol, penetration, resolution, selector):
        """ EveningStar(self: CandlestickPatterns, symbol: Symbol, penetration: Decimal, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> EveningStar """
        pass

    def GapSideBySideWhite(self, symbol, resolution, selector):
        """ GapSideBySideWhite(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> GapSideBySideWhite """
        pass

    def GravestoneDoji(self, symbol, resolution, selector):
        """ GravestoneDoji(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> GravestoneDoji """
        pass

    def Hammer(self, symbol, resolution, selector):
        """ Hammer(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> Hammer """
        pass

    def HangingMan(self, symbol, resolution, selector):
        """ HangingMan(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> HangingMan """
        pass

    def Harami(self, symbol, resolution, selector):
        """ Harami(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> Harami """
        pass

    def HaramiCross(self, symbol, resolution, selector):
        """ HaramiCross(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> HaramiCross """
        pass

    def HighWaveCandle(self, symbol, resolution, selector):
        """ HighWaveCandle(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> HighWaveCandle """
        pass

    def Hikkake(self, symbol, resolution, selector):
        """ Hikkake(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> Hikkake """
        pass

    def HikkakeModified(self, symbol, resolution, selector):
        """ HikkakeModified(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> HikkakeModified """
        pass

    def HomingPigeon(self, symbol, resolution, selector):
        """ HomingPigeon(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> HomingPigeon """
        pass

    def IdenticalThreeCrows(self, symbol, resolution, selector):
        """ IdenticalThreeCrows(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> IdenticalThreeCrows """
        pass

    def InNeck(self, symbol, resolution, selector):
        """ InNeck(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> InNeck """
        pass

    def InvertedHammer(self, symbol, resolution, selector):
        """ InvertedHammer(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> InvertedHammer """
        pass

    def Kicking(self, symbol, resolution, selector):
        """ Kicking(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> Kicking """
        pass

    def KickingByLength(self, symbol, resolution, selector):
        """ KickingByLength(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> KickingByLength """
        pass

    def LadderBottom(self, symbol, resolution, selector):
        """ LadderBottom(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> LadderBottom """
        pass

    def LongLeggedDoji(self, symbol, resolution, selector):
        """ LongLeggedDoji(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> LongLeggedDoji """
        pass

    def LongLineCandle(self, symbol, resolution, selector):
        """ LongLineCandle(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> LongLineCandle """
        pass

    def Marubozu(self, symbol, resolution, selector):
        """ Marubozu(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> Marubozu """
        pass

    def MatchingLow(self, symbol, resolution, selector):
        """ MatchingLow(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> MatchingLow """
        pass

    def MatHold(self, symbol, penetration, resolution, selector):
        """ MatHold(self: CandlestickPatterns, symbol: Symbol, penetration: Decimal, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> MatHold """
        pass

    def MorningDojiStar(self, symbol, penetration, resolution, selector):
        """ MorningDojiStar(self: CandlestickPatterns, symbol: Symbol, penetration: Decimal, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> MorningDojiStar """
        pass

    def MorningStar(self, symbol, penetration, resolution, selector):
        """ MorningStar(self: CandlestickPatterns, symbol: Symbol, penetration: Decimal, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> MorningStar """
        pass

    def OnNeck(self, symbol, resolution, selector):
        """ OnNeck(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> OnNeck """
        pass

    def Piercing(self, symbol, resolution, selector):
        """ Piercing(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> Piercing """
        pass

    def RickshawMan(self, symbol, resolution, selector):
        """ RickshawMan(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> RickshawMan """
        pass

    def RiseFallThreeMethods(self, symbol, resolution, selector):
        """ RiseFallThreeMethods(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> RiseFallThreeMethods """
        pass

    def SeparatingLines(self, symbol, resolution, selector):
        """ SeparatingLines(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> SeparatingLines """
        pass

    def ShootingStar(self, symbol, resolution, selector):
        """ ShootingStar(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> ShootingStar """
        pass

    def ShortLineCandle(self, symbol, resolution, selector):
        """ ShortLineCandle(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> ShortLineCandle """
        pass

    def SpinningTop(self, symbol, resolution, selector):
        """ SpinningTop(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> SpinningTop """
        pass

    def StalledPattern(self, symbol, resolution, selector):
        """ StalledPattern(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> StalledPattern """
        pass

    def StickSandwich(self, symbol, resolution, selector):
        """ StickSandwich(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> StickSandwich """
        pass

    def Takuri(self, symbol, resolution, selector):
        """ Takuri(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> Takuri """
        pass

    def TasukiGap(self, symbol, resolution, selector):
        """ TasukiGap(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> TasukiGap """
        pass

    def ThreeBlackCrows(self, symbol, resolution, selector):
        """ ThreeBlackCrows(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> ThreeBlackCrows """
        pass

    def ThreeInside(self, symbol, resolution, selector):
        """ ThreeInside(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> ThreeInside """
        pass

    def ThreeLineStrike(self, symbol, resolution, selector):
        """ ThreeLineStrike(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> ThreeLineStrike """
        pass

    def ThreeOutside(self, symbol, resolution, selector):
        """ ThreeOutside(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> ThreeOutside """
        pass

    def ThreeStarsInSouth(self, symbol, resolution, selector):
        """ ThreeStarsInSouth(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> ThreeStarsInSouth """
        pass

    def ThreeWhiteSoldiers(self, symbol, resolution, selector):
        """ ThreeWhiteSoldiers(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> ThreeWhiteSoldiers """
        pass

    def Thrusting(self, symbol, resolution, selector):
        """ Thrusting(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> Thrusting """
        pass

    def Tristar(self, symbol, resolution, selector):
        """ Tristar(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> Tristar """
        pass

    def TwoCrows(self, symbol, resolution, selector):
        """ TwoCrows(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> TwoCrows """
        pass

    def UniqueThreeRiver(self, symbol, resolution, selector):
        """ UniqueThreeRiver(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> UniqueThreeRiver """
        pass

    def UpDownGapThreeMethods(self, symbol, resolution, selector):
        """ UpDownGapThreeMethods(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> UpDownGapThreeMethods """
        pass

    def UpsideGapTwoCrows(self, symbol, resolution, selector):
        """ UpsideGapTwoCrows(self: CandlestickPatterns, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> UpsideGapTwoCrows """
        pass

    @staticmethod # known case of __new__
    def __new__(self, algorithm):
        """ __new__(cls: type, algorithm: QCAlgorithm) """
        pass


class ConstituentUniverseDefinitions(object):
    """
    Provides helpers for defining constituent universes based on the Morningstar

                asset classification QuantConnect.Data.Fundamental.AssetClassification https://www.morningstar.com/

    

    ConstituentUniverseDefinitions(algorithm: IAlgorithm)
    """
    def AerospaceAndDefense(self, universeSettings):
        """
        AerospaceAndDefense(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar AerospaceAndDefense industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def AggressiveGrowth(self, universeSettings):
        """
        AggressiveGrowth(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Universe which selects companies whose revenues 

             and earnings have both been growing significantly 

             faster than

                    the general economy.
        """
        pass

    def Agriculture(self, universeSettings):
        """
        Agriculture(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar Agriculture industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def AssetManagement(self, universeSettings):
        """
        AssetManagement(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar AssetManagement industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def Banks(self, universeSettings):
        """
        Banks(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar Banks industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def BeveragesAlcoholic(self, universeSettings):
        """
        BeveragesAlcoholic(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar BeveragesAlcoholic industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def BeveragesNonAlcoholic(self, universeSettings):
        """
        BeveragesNonAlcoholic(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar BeveragesNonAlcoholic industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def Biotechnology(self, universeSettings):
        """
        Biotechnology(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar Biotechnology industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def BuildingMaterials(self, universeSettings):
        """
        BuildingMaterials(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar BuildingMaterials industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def BusinessServices(self, universeSettings):
        """
        BusinessServices(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar BusinessServices industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def CapitalMarkets(self, universeSettings):
        """
        CapitalMarkets(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar CapitalMarkets industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def Chemicals(self, universeSettings):
        """
        Chemicals(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar Chemicals industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def ClassicGrowth(self, universeSettings):
        """
        ClassicGrowth(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Universe which selects companies that are growing 

             respectably faster than the general economy, and 

             often pay a

                    steady dividend. They 

             tend to be mature and solidly profitable 

             businesses.
        """
        pass

    def Conglomerates(self, universeSettings):
        """
        Conglomerates(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar Conglomerates industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def Construction(self, universeSettings):
        """
        Construction(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar Construction industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def ConsumerPackagedGoods(self, universeSettings):
        """
        ConsumerPackagedGoods(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar ConsumerPackagedGoods industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def CreditServices(self, universeSettings):
        """
        CreditServices(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar CreditServices industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def Cyclicals(self, universeSettings):
        """
        Cyclicals(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Universe which selects companies in the cyclicals 

             and durables sectors, except those in the three 

             types below.

                    The profits of 

             cyclicals tend to rise and fall with the general 

             economy.
        """
        pass

    def Distressed(self, universeSettings):
        """
        Distressed(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Universe which selects companies that have had 

             consistently declining cash flows and earnings 

             over the past

                    three years, and/or 

             very high debt.
        """
        pass

    def DiversifiedFinancialServices(self, universeSettings):
        """
        DiversifiedFinancialServices(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar DiversifiedFinancialServices industry 

             group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def DrugManufacturers(self, universeSettings):
        """
        DrugManufacturers(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar DrugManufacturers industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def Education(self, universeSettings):
        """
        Education(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar Education industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def FarmAndHeavyConstructionMachinery(self, universeSettings):
        """
        FarmAndHeavyConstructionMachinery(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar FarmAndHeavyConstructionMachinery 

             industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def FixturesAndAppliances(self, universeSettings):
        """
        FixturesAndAppliances(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar FixturesAndAppliances industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def ForestProducts(self, universeSettings):
        """
        ForestProducts(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar ForestProducts industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def HardAsset(self, universeSettings):
        """
        HardAsset(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Universe which selects companies that deal in 

             assets such as oil, metals, and real estate, 

             which tend to do

                    well in 

             inflationary environments.
        """
        pass

    def Hardware(self, universeSettings):
        """
        Hardware(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar Hardware industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def HealthcarePlans(self, universeSettings):
        """
        HealthcarePlans(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar HealthcarePlans industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def HealthcareProvidersAndServices(self, universeSettings):
        """
        HealthcareProvidersAndServices(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar HealthcareProvidersAndServices 

             industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def HighYield(self, universeSettings):
        """
        HighYield(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Universe which selects companies that have 

             dividend yields at least twice the average for 

             large-cap stocks.

                    They tend to be 

             mature, slow-growing companies.
        """
        pass

    def HomebuildingAndConstruction(self, universeSettings):
        """
        HomebuildingAndConstruction(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar HomebuildingAndConstruction industry 

             group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def IndustrialDistribution(self, universeSettings):
        """
        IndustrialDistribution(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar IndustrialDistribution industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def IndustrialProducts(self, universeSettings):
        """
        IndustrialProducts(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar IndustrialProducts industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def Insurance(self, universeSettings):
        """
        Insurance(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar Insurance industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def InteractiveMedia(self, universeSettings):
        """
        InteractiveMedia(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar InteractiveMedia industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def LargeCore(self, universeSettings):
        """
        LargeCore(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Classifies securities according to market 

             capitalization and growth and value factor
        """
        pass

    def LargeGrowth(self, universeSettings):
        """
        LargeGrowth(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Classifies securities according to market 

             capitalization and growth and value factor
        """
        pass

    def LargeValue(self, universeSettings):
        """
        LargeValue(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Classifies securities according to market 

             capitalization and growth and value factor
        """
        pass

    def ManufacturingApparelAndAccessories(self, universeSettings):
        """
        ManufacturingApparelAndAccessories(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar ManufacturingApparelAndAccessories 

             industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def MediaDiversified(self, universeSettings):
        """
        MediaDiversified(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar MediaDiversified industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def MedicalDevicesAndInstruments(self, universeSettings):
        """
        MedicalDevicesAndInstruments(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar MedicalDevicesAndInstruments industry 

             group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def MedicalDiagnosticsAndResearch(self, universeSettings):
        """
        MedicalDiagnosticsAndResearch(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar MedicalDiagnosticsAndResearch 

             industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def MedicalDistribution(self, universeSettings):
        """
        MedicalDistribution(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar MedicalDistribution industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def MetalsAndMining(self, universeSettings):
        """
        MetalsAndMining(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar MetalsAndMining industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def MidCore(self, universeSettings):
        """
        MidCore(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Classifies securities according to market 

             capitalization and growth and value factor
        """
        pass

    def MidGrowth(self, universeSettings):
        """
        MidGrowth(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Classifies securities according to market 

             capitalization and growth and value factor
        """
        pass

    def MidValue(self, universeSettings):
        """
        MidValue(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Classifies securities according to market 

             capitalization and growth and value factor
        """
        pass

    def OilAndGas(self, universeSettings):
        """
        OilAndGas(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar OilAndGas industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def OtherEnergySources(self, universeSettings):
        """
        OtherEnergySources(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar OtherEnergySources industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def PackagingAndContainers(self, universeSettings):
        """
        PackagingAndContainers(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar PackagingAndContainers industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def PersonalServices(self, universeSettings):
        """
        PersonalServices(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar PersonalServices industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def RealEstate(self, universeSettings):
        """
        RealEstate(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar RealEstate industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def REITs(self, universeSettings):
        """
        REITs(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar REITs industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def Restaurants(self, universeSettings):
        """
        Restaurants(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar Restaurants industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def RetailCyclical(self, universeSettings):
        """
        RetailCyclical(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar RetailCyclical industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def RetailDefensive(self, universeSettings):
        """
        RetailDefensive(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar RetailDefensive industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def Semiconductors(self, universeSettings):
        """
        Semiconductors(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar Semiconductors industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def SlowGrowth(self, universeSettings):
        """
        SlowGrowth(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Universe which selects companies that have shown 

             slow revenue and earnings growth (typically less 

             than the rate

                    of GDP growth) over at 

             least three years.
        """
        pass

    def SmallCore(self, universeSettings):
        """
        SmallCore(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Classifies securities according to market 

             capitalization and growth and value factor
        """
        pass

    def SmallGrowth(self, universeSettings):
        """
        SmallGrowth(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Classifies securities according to market 

             capitalization and growth and value factor
        """
        pass

    def SmallValue(self, universeSettings):
        """
        SmallValue(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Classifies securities according to market 

             capitalization and growth and value factor
        """
        pass

    def Software(self, universeSettings):
        """
        Software(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar Software industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def SpeculativeGrowth(self, universeSettings):
        """
        SpeculativeGrowth(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Universe which selects companies that have shown 

             strong revenue growth but slower or spotty 

             earnings growth.

                    Very small or young 

             companies also tend to fall into this class.
        """
        pass

    def Steel(self, universeSettings):
        """
        Steel(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar Steel industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def TelecommunicationServices(self, universeSettings):
        """
        TelecommunicationServices(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar TelecommunicationServices industry 

             group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def TobaccoProducts(self, universeSettings):
        """
        TobaccoProducts(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar TobaccoProducts industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def Transportation(self, universeSettings):
        """
        Transportation(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar Transportation industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def TravelAndLeisure(self, universeSettings):
        """
        TravelAndLeisure(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar TravelAndLeisure industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def UtilitiesIndependentPowerProducers(self, universeSettings):
        """
        UtilitiesIndependentPowerProducers(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar UtilitiesIndependentPowerProducers 

             industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def UtilitiesRegulated(self, universeSettings):
        """
        UtilitiesRegulated(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar UtilitiesRegulated industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def VehiclesAndParts(self, universeSettings):
        """
        VehiclesAndParts(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar VehiclesAndParts industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    def WasteManagement(self, universeSettings):
        """
        WasteManagement(self: ConstituentUniverseDefinitions, universeSettings: UniverseSettings) -> Universe

        

            Morningstar WasteManagement industry group 

             QuantConnect.Data.Fundamental.MorningstarIndustryG

             roupCode
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, algorithm):
        """ __new__(cls: type, algorithm: IAlgorithm) """
        pass


class DollarVolumeUniverseDefinitions(object):
    """
    Provides helpers for defining universes based on the daily dollar volume

    

    DollarVolumeUniverseDefinitions(algorithm: QCAlgorithm)
    """
    def Bottom(self, count, universeSettings):
        """
        Bottom(self: DollarVolumeUniverseDefinitions, count: int, universeSettings: UniverseSettings) -> Universe

        

            Creates a new coarse universe that contains the 

             bottom count of stocks

                    by daily 

             dollar volume

        

        

            count: The number of stock to select

            universeSettings: The settings for stocks added by this universe.

         

                        Defaults to 

             QuantConnect.Algorithm.QCAlgorithm.UniverseSetting

             s

        

            Returns: A new coarse universe for the bottom count of 

             stocks by dollar volume
        """
        pass

    def Percentile(self, *__args):
        """
        Percentile(self: DollarVolumeUniverseDefinitions, percentile: float, universeSettings: UniverseSettings) -> Universe

        

            Creates a new coarse universe that contains 

             stocks in the specified

                    dollar 

             volume percentile

        

        

            percentile: The desired dollar volume percentile (0 to 100 

             inclusive)

        

            universeSettings: The settings for stocks added by this universe.

         

                        Defaults to 

             QuantConnect.Algorithm.QCAlgorithm.UniverseSetting

             s

        

            Returns: A new coarse universe for the bottom count of 

             stocks by dollar volume

        

        Percentile(self: DollarVolumeUniverseDefinitions, lowerPercentile: float, upperPercentile: float, universeSettings: UniverseSettings) -> Universe

        

            Creates a new coarse universe that contains 

             stocks in the specified dollar volume percentile 

             range,

                    that is, this universe will 

             produce stocks with dollar volumes between the 

             lower percentile bound

                    and the upper 

             percentile bound

        

        

            lowerPercentile: The desired lower dollar volume  percentile bound 

             (0 to 100 inclusive)

        

            upperPercentile: The desired upper dollar volume  percentile bound 

             (0 to 100 inclusive)

        

            universeSettings: The settings for stocks added by this universe.

         

                        Defaults to 

             QuantConnect.Algorithm.QCAlgorithm.UniverseSetting

             s

        

            Returns: A new coarse universe for the bottom count of 

             stocks by dollar volume
        """
        pass

    def Top(self, count, universeSettings):
        """
        Top(self: DollarVolumeUniverseDefinitions, count: int, universeSettings: UniverseSettings) -> Universe

        

            Creates a new coarse universe that contains the 

             top count of stocks

                    by daily dollar 

             volume

        

        

            count: The number of stock to select

            universeSettings: The settings for stocks added by this universe.

         

                        Defaults to 

             QuantConnect.Algorithm.QCAlgorithm.UniverseSetting

             s

        

            Returns: A new coarse universe for the top count of stocks 

             by dollar volume
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, algorithm):
        """ __new__(cls: type, algorithm: QCAlgorithm) """
        pass


class IndexUniverseDefinitions(object):
    """
    Provides helpers for defining universes based on index definitions

    

    IndexUniverseDefinitions(algorithm: QCAlgorithm)
    """
    @staticmethod # known case of __new__
    def __new__(self, algorithm):
        """ __new__(cls: type, algorithm: QCAlgorithm) """
        pass

    QC500 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Creates a new fine universe that contains the constituents of QC500 index based onthe company fundamentals

            The algorithm creates a default tradable and liquid universe containing 500 US equities

            which are chosen at the first trading day of each month.



Get: QC500(self: IndexUniverseDefinitions) -> Universe



"""



class QCAlgorithm(MarshalByRefObject, IAlgorithm, ISecurityInitializerProvider, IAccountCurrencyProvider):
    """
    QC Algorithm Base Class - Handle the basic requirements of a trading algorithm,

                allowing user to focus on event methods. The QCAlgorithm class implements Portfolio,

                Securities, Transactions and Data Subscription Management.

    

    QCAlgorithm()
    """
    def ABANDS(self, symbol, period, width, movingAverageType, resolution, selector):
        """ ABANDS(self: QCAlgorithm, symbol: Symbol, period: int, width: Decimal, movingAverageType: MovingAverageType, resolution: Nullable[Resolution], selector: Func[IBaseData, TradeBar]) -> AccelerationBands """
        pass

    def AD(self, symbol, resolution, selector):
        """ AD(self: QCAlgorithm, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, TradeBar]) -> AccumulationDistribution """
        pass

    def AddAlpha(self, alpha):
        """
        AddAlpha(self: QCAlgorithm, alpha: PyObject)

            Adds a new alpha model

        

            alpha: Model that generates alpha to add

        AddAlpha(self: QCAlgorithm, alpha: IAlphaModel)

            Adds a new alpha model

        

            alpha: Model that generates alpha to add
        """
        pass

    def AddCfd(self, ticker, resolution, market, fillDataForward, leverage):
        """ AddCfd(self: QCAlgorithm, ticker: str, resolution: Nullable[Resolution], market: str, fillDataForward: bool, leverage: Decimal) -> Cfd """
        pass

    def AddChart(self, chart):
        """
        AddChart(self: QCAlgorithm, chart: Chart)

            Add a Chart object to algorithm collection

        

            chart: Chart object to add to collection.
        """
        pass

    def AddCrypto(self, ticker, resolution, market, fillDataForward, leverage):
        """ AddCrypto(self: QCAlgorithm, ticker: str, resolution: Nullable[Resolution], market: str, fillDataForward: bool, leverage: Decimal) -> Crypto """
        pass

    def AddData(self, *__args):
        """
        AddData(self: QCAlgorithm, type: PyObject, ticker: str, resolution: Nullable[Resolution]) -> Security

        AddData(self: QCAlgorithm, type: PyObject, underlying: Symbol, resolution: Nullable[Resolution]) -> Security

        AddData(self: QCAlgorithm, type: PyObject, ticker: str, resolution: Nullable[Resolution], timeZone: DateTimeZone, fillDataForward: bool, leverage: Decimal) -> Security

        AddData(self: QCAlgorithm, type: PyObject, underlying: Symbol, resolution: Nullable[Resolution], timeZone: DateTimeZone, fillDataForward: bool, leverage: Decimal) -> Security

        AddData(self: QCAlgorithm, dataType: Type, ticker: str, resolution: Nullable[Resolution], timeZone: DateTimeZone, fillDataForward: bool, leverage: Decimal) -> Security

        AddData(self: QCAlgorithm, dataType: Type, underlying: Symbol, resolution: Nullable[Resolution], timeZone: DateTimeZone, fillDataForward: bool, leverage: Decimal) -> Security

        AddData[T](self: QCAlgorithm, ticker: str, resolution: Nullable[Resolution]) -> Security

        AddData[T](self: QCAlgorithm, underlying: Symbol, resolution: Nullable[Resolution]) -> Security

        AddData[T](self: QCAlgorithm, ticker: str, resolution: Nullable[Resolution], fillDataForward: bool, leverage: Decimal) -> Security

        AddData[T](self: QCAlgorithm, underlying: Symbol, resolution: Nullable[Resolution], fillDataForward: bool, leverage: Decimal) -> Security

        AddData[T](self: QCAlgorithm, ticker: str, resolution: Nullable[Resolution], timeZone: DateTimeZone, fillDataForward: bool, leverage: Decimal) -> Security

        AddData[T](self: QCAlgorithm, underlying: Symbol, resolution: Nullable[Resolution], timeZone: DateTimeZone, fillDataForward: bool, leverage: Decimal) -> Security
        """
        pass

    def AddEquity(self, ticker, resolution, market, fillDataForward, leverage, extendedMarketHours):
        """ AddEquity(self: QCAlgorithm, ticker: str, resolution: Nullable[Resolution], market: str, fillDataForward: bool, leverage: Decimal, extendedMarketHours: bool) -> Equity """
        pass

    def AddForex(self, ticker, resolution, market, fillDataForward, leverage):
        """ AddForex(self: QCAlgorithm, ticker: str, resolution: Nullable[Resolution], market: str, fillDataForward: bool, leverage: Decimal) -> Forex """
        pass

    def AddFuture(self, ticker, resolution, market, fillDataForward, leverage):
        """ AddFuture(self: QCAlgorithm, ticker: str, resolution: Nullable[Resolution], market: str, fillDataForward: bool, leverage: Decimal) -> Future """
        pass

    def AddFutureContract(self, symbol, resolution, fillDataForward, leverage):
        """ AddFutureContract(self: QCAlgorithm, symbol: Symbol, resolution: Nullable[Resolution], fillDataForward: bool, leverage: Decimal) -> Future """
        pass

    def AddOption(self, underlying, resolution, market, fillDataForward, leverage):
        """ AddOption(self: QCAlgorithm, underlying: str, resolution: Nullable[Resolution], market: str, fillDataForward: bool, leverage: Decimal) -> Option """
        pass

    def AddOptionContract(self, symbol, resolution, fillDataForward, leverage):
        """ AddOptionContract(self: QCAlgorithm, symbol: Symbol, resolution: Nullable[Resolution], fillDataForward: bool, leverage: Decimal) -> Option """
        pass

    def AddRiskManagement(self, riskManagement):
        """
        AddRiskManagement(self: QCAlgorithm, riskManagement: PyObject)

            Adds a new risk management model

        

            riskManagement: Model defining how risk is managed to add

        AddRiskManagement(self: QCAlgorithm, riskManagement: IRiskManagementModel)

            Adds a new risk management model

        

            riskManagement: Model defining how risk is managed to add
        """
        pass

    def AddSecurity(self, *__args):
        """
        AddSecurity(self: QCAlgorithm, securityType: SecurityType, ticker: str, resolution: Nullable[Resolution], fillDataForward: bool, extendedMarketHours: bool) -> Security

        AddSecurity(self: QCAlgorithm, securityType: SecurityType, ticker: str, resolution: Nullable[Resolution], fillDataForward: bool, leverage: Decimal, extendedMarketHours: bool) -> Security

        AddSecurity(self: QCAlgorithm, securityType: SecurityType, ticker: str, resolution: Nullable[Resolution], market: str, fillDataForward: bool, leverage: Decimal, extendedMarketHours: bool) -> Security

        AddSecurity(self: QCAlgorithm, symbol: Symbol, resolution: Nullable[Resolution], fillDataForward: bool, leverage: Decimal, extendedMarketHours: bool) -> Security
        """
        pass

    def AddSeries(self, chart, series, seriesType, unit):
        """
        AddSeries(self: QCAlgorithm, chart: str, series: str, seriesType: SeriesType, unit: str)

            Add a series object for charting. This is useful 

             when initializing charts with

                    series 

             other than type = line. If a series exists in the 

             chart with the same name,

                    then it is 

             replaced.

        

        

            chart: The chart name

            series: The series name

            seriesType: The type of series, i.e, Scatter

            unit: The unit of the y axis, usually $
        """
        pass

    def AddUniverse(self, *__args):
        """
        AddUniverse[T](self: QCAlgorithm, securityType: SecurityType, name: str, resolution: Resolution, market: str, selector: Func[IEnumerable[T], IEnumerable[str]])AddUniverse(self: QCAlgorithm, T: PyObject, securityType: SecurityType, name: str, resolution: Resolution, market: str, selector: PyObject)

            Creates a new universe and adds it to the 

             algorithm. This will use the default universe 

             settings

                    specified via the 

             QuantConnect.Algorithm.QCAlgorithm.UniverseSetting

             s property.

        

        

            T: The data type

            securityType: The security type the universe produces

            name: A unique name for this universe

            resolution: The epected resolution of the universe data

            market: The market for selected symbols

            selector: Function delegate that performs selection on the 

             universe data

        

        AddUniverse(self: QCAlgorithm, T: PyObject, name: str, universeSettings: UniverseSettings, selector: PyObject)

            Creates a new universe and adds it to the 

             algorithm. This will use the default universe 

             settings

                    specified via the 

             QuantConnect.Algorithm.QCAlgorithm.UniverseSetting

             s property. This universe will use the defaults

         

                        of SecurityType.Equity, 

             Resolution.Daily, and Market.USA

        

        

            T: The data type

            name: A unique name for this universe

            universeSettings: The settings used for securities added by this 

             universe

        

            selector: Function delegate that performs selection on the 

             universe data

        

        AddUniverse(self: QCAlgorithm, T: PyObject, name: str, resolution: Resolution, universeSettings: UniverseSettings, selector: PyObject)

            Creates a new universe and adds it to the 

             algorithm. This will use the default universe 

             settings

                    specified via the 

             QuantConnect.Algorithm.QCAlgorithm.UniverseSetting

             s property. This universe will use the defaults

         

                        of SecurityType.Equity, and Market.USA

        

        

            T: The data type

            name: A unique name for this universe

            resolution: The epected resolution of the universe data

            universeSettings: The settings used for securities added by this 

             universe

        

            selector: Function delegate that performs selection on the 

             universe data

        

        AddUniverse(self: QCAlgorithm, T: PyObject, name: str, resolution: Resolution, selector: PyObject)

            Creates a new universe and adds it to the 

             algorithm. This will use the default universe 

             settings

                    specified via the 

             QuantConnect.Algorithm.QCAlgorithm.UniverseSetting

             s property. This universe will use the defaults

         

                        of SecurityType.Equity, Market.USA and 

             UniverseSettings

        

        

            T: The data type

            name: A unique name for this universe

            resolution: The epected resolution of the universe data

            selector: Function delegate that performs selection on the 

             universe data

        

        AddUniverse(self: QCAlgorithm, T: PyObject, name: str, selector: PyObject)

            Creates a new universe and adds it to the 

             algorithm. This will use the default universe 

             settings

                    specified via the 

             QuantConnect.Algorithm.QCAlgorithm.UniverseSetting

             s property. This universe will use the defaults

         

                        of SecurityType.Equity, 

             Resolution.Daily, Market.USA, and 

             UniverseSettings

        

        

            T: The data type

            name: A unique name for this universe

            selector: Function delegate that performs selection on the 

             universe data

        

        AddUniverse(self: QCAlgorithm, securityType: SecurityType, name: str, resolution: Resolution, market: str, universeSettings: UniverseSettings, pySelector: PyObject)

            Creates a new user defined universe that will 

             fire on the requested resolution during market 

             hours.

        

        

            securityType: The security type of the universe

            name: A unique name for this universe

            resolution: The resolution this universe should be triggered 

             on

        

            market: The market of the universe

            universeSettings: The subscription settings used for securities 

             added from this universe

        

            pySelector: Function delegate that accepts a DateTime and 

             returns a collection of string symbols

        

        AddUniverse(self: QCAlgorithm, name: str, pySelector: PyObject)

            Creates a new universe and adds it to the 

             algorithm. This can be used to return a list of 

             string

                    symbols retrieved from 

             anywhere and will loads those symbols under the 

             US Equity market.

        

        

            name: A unique name for this universe

            pySelector: Function delegate that accepts a DateTime and 

             returns a collection of string symbols

        

        AddUniverse(self: QCAlgorithm, name: str, resolution: Resolution, pySelector: PyObject)

            Creates a new universe and adds it to the 

             algorithm. This can be used to return a list of 

             string

                    symbols retrieved from 

             anywhere and will loads those symbols under the 

             US Equity market.

        

        

            name: A unique name for this universe

            resolution: The resolution this universe should be triggered 

             on

        

            pySelector: Function delegate that accepts a DateTime and 

             returns a collection of string symbols

        

        AddUniverse(self: QCAlgorithm, pyObject: PyObject, pyfine: PyObject)

            Creates a new universe and adds it to the 

             algorithm. This is for coarse and fine 

             fundamental US Equity data and

                    will 

             be executed on day changes in the NewYork time 

             zone (QuantConnect.TimeZones.NewYork

        

        

            pyObject: Defines an initial coarse selection or a universe

            pyfine: Defines a more detailed selection with access to 

             more data

        

        AddUniverse(self: QCAlgorithm, pyObject: PyObject)

            Creates a new universe and adds it to the 

             algorithm. This is for coarse fundamental US 

             Equity data and

                    will be executed on 

             day changes in the NewYork time zone 

             (QuantConnect.TimeZones.NewYork

        

        

            pyObject: Defines an initial coarse selection

        AddUniverse[T](self: QCAlgorithm, securityType: SecurityType, name: str, resolution: Resolution, market: str, selector: Func[IEnumerable[T], IEnumerable[Symbol]])AddUniverse[T](self: QCAlgorithm, name: str, resolution: Resolution, universeSettings: UniverseSettings, selector: Func[IEnumerable[T], IEnumerable[str]])AddUniverse[T](self: QCAlgorithm, name: str, resolution: Resolution, universeSettings: UniverseSettings, selector: Func[IEnumerable[T], IEnumerable[Symbol]])AddUniverse(self: QCAlgorithm, T: PyObject, securityType: SecurityType, name: str, resolution: Resolution, market: str, universeSettings: UniverseSettings, selector: PyObject)

            Creates a new universe and adds it to the 

             algorithm

        

        

            T: The data type

            securityType: The security type the universe produces

            name: A unique name for this universe

            resolution: The epected resolution of the universe data

            market: The market for selected symbols

            universeSettings: The subscription settings to use for newly 

             created subscriptions

        

            selector: Function delegate that performs selection on the 

             universe data

        

        AddUniverse[T](self: QCAlgorithm, name: str, resolution: Resolution, selector: Func[IEnumerable[T], IEnumerable[str]])AddUniverse[T](self: QCAlgorithm, name: str, universeSettings: UniverseSettings, selector: Func[IEnumerable[T], IEnumerable[str]])AddUniverse[T](self: QCAlgorithm, name: str, universeSettings: UniverseSettings, selector: Func[IEnumerable[T], IEnumerable[Symbol]])AddUniverse[T](self: QCAlgorithm, name: str, selector: Func[IEnumerable[T], IEnumerable[str]])AddUniverse[T](self: QCAlgorithm, name: str, selector: Func[IEnumerable[T], IEnumerable[Symbol]])AddUniverse(self: QCAlgorithm, universe: Universe)

            Adds the universe to the algorithm

        

            universe: The universe to be added

        AddUniverse(self: QCAlgorithm, securityType: SecurityType, name: str, resolution: Resolution, market: str, universeSettings: UniverseSettings, selector: Func[DateTime, IEnumerable[str]])AddUniverse(self: QCAlgorithm, name: str, resolution: Resolution, selector: Func[DateTime, IEnumerable[str]])AddUniverse(self: QCAlgorithm, name: str, selector: Func[DateTime, IEnumerable[str]])AddUniverse(self: QCAlgorithm, universe: Universe, fineSelector: Func[IEnumerable[FineFundamental], IEnumerable[Symbol]])AddUniverse(self: QCAlgorithm, coarseSelector: Func[IEnumerable[CoarseFundamental], IEnumerable[Symbol]], fineSelector: Func[IEnumerable[FineFundamental], IEnumerable[Symbol]])AddUniverse(self: QCAlgorithm, selector: Func[IEnumerable[CoarseFundamental], IEnumerable[Symbol]])AddUniverse[T](self: QCAlgorithm, securityType: SecurityType, name: str, resolution: Resolution, market: str, universeSettings: UniverseSettings, selector: Func[IEnumerable[T], IEnumerable[str]])AddUniverse[T](self: QCAlgorithm, securityType: SecurityType, name: str, resolution: Resolution, market: str, universeSettings: UniverseSettings, selector: Func[IEnumerable[T], IEnumerable[Symbol]])AddUniverse[T](self: QCAlgorithm, name: str, resolution: Resolution, selector: Func[IEnumerable[T], IEnumerable[Symbol]])AddUniverse(self: QCAlgorithm, dataType: Type, securityType: SecurityType, name: str, resolution: Resolution, market: str, universeSettings: UniverseSettings, pySelector: PyObject)

            Creates a new universe and adds it to the 

             algorithm

        

        

            dataType: The data type

            securityType: The security type the universe produces

            name: A unique name for this universe

            resolution: The epected resolution of the universe data

            market: The market for selected symbols

            universeSettings: The subscription settings to use for newly 

             created subscriptions

        

            pySelector: Function delegate that performs selection on the 

             universe data
        """
        pass

    def AddUniverseSelection(self, universeSelection):
        """
        AddUniverseSelection(self: QCAlgorithm, universeSelection: PyObject)

            Adds a new universe selection model

        

            universeSelection: Model defining universes for the algorithm to add

        AddUniverseSelection(self: QCAlgorithm, universeSelection: IUniverseSelectionModel)

            Adds a new universe selection model

        

            universeSelection: Model defining universes for the algorithm to add
        """
        pass

    def ADOSC(self, symbol, fastPeriod, slowPeriod, resolution, selector):
        """ ADOSC(self: QCAlgorithm, symbol: Symbol, fastPeriod: int, slowPeriod: int, resolution: Nullable[Resolution], selector: Func[IBaseData, TradeBar]) -> AccumulationDistributionOscillator """
        pass

    def ADX(self, symbol, period, resolution, selector):
        """ ADX(self: QCAlgorithm, symbol: Symbol, period: int, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> AverageDirectionalIndex """
        pass

    def ADXR(self, symbol, period, resolution, selector):
        """ ADXR(self: QCAlgorithm, symbol: Symbol, period: int, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> AverageDirectionalMovementIndexRating """
        pass

    def ALMA(self, symbol, period, sigma, offset, resolution, selector):
        """ ALMA(self: QCAlgorithm, symbol: Symbol, period: int, sigma: int, offset: Decimal, resolution: Nullable[Resolution], selector: Func[IBaseData, Decimal]) -> ArnaudLegouxMovingAverage """
        pass

    def APO(self, symbol, fastPeriod, slowPeriod, movingAverageType, resolution, selector):
        """ APO(self: QCAlgorithm, symbol: Symbol, fastPeriod: int, slowPeriod: int, movingAverageType: MovingAverageType, resolution: Nullable[Resolution], selector: Func[IBaseData, Decimal]) -> AbsolutePriceOscillator """
        pass

    def AROON(self, symbol, *__args):
        """
        AROON(self: QCAlgorithm, symbol: Symbol, period: int, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> AroonOscillator

        AROON(self: QCAlgorithm, symbol: Symbol, upPeriod: int, downPeriod: int, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> AroonOscillator
        """
        pass

    def ATR(self, symbol, period, type, resolution, selector):
        """ ATR(self: QCAlgorithm, symbol: Symbol, period: int, type: MovingAverageType, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> AverageTrueRange """
        pass

    def BB(self, symbol, period, k, movingAverageType, resolution, selector):
        """ BB(self: QCAlgorithm, symbol: Symbol, period: int, k: Decimal, movingAverageType: MovingAverageType, resolution: Nullable[Resolution], selector: Func[IBaseData, Decimal]) -> BollingerBands """
        pass

    def BOP(self, symbol, resolution, selector):
        """ BOP(self: QCAlgorithm, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> BalanceOfPower """
        pass

    def Buy(self, *__args):
        """
        Buy(self: QCAlgorithm, symbol: Symbol, quantity: int) -> OrderTicket

        

            Buy Stock (Alias of Order)

        

            symbol: string Symbol of the asset to trade

            quantity: int Quantity of the asset to trade

        Buy(self: QCAlgorithm, symbol: Symbol, quantity: float) -> OrderTicket

        

            Buy Stock (Alias of Order)

        

            symbol: string Symbol of the asset to trade

            quantity: double Quantity of the asset to trade

        Buy(self: QCAlgorithm, symbol: Symbol, quantity: Decimal) -> OrderTicket

        

            Buy Stock (Alias of Order)

        

            symbol: string Symbol of the asset to trade

            quantity: decimal Quantity of the asset to trade

        Buy(self: QCAlgorithm, symbol: Symbol, quantity: Single) -> OrderTicket

        

            Buy Stock (Alias of Order)

        

            symbol: string Symbol of the asset to trade

            quantity: float Quantity of the asset to trade

        Buy(self: QCAlgorithm, strategy: OptionStrategy, quantity: int) -> IEnumerable[OrderTicket]

        

            Buy Option Strategy (Alias of Order)

        

            strategy: Specification of the strategy to trade

            quantity: Quantity of the strategy to trade

            Returns: Sequence of order ids
        """
        pass

    def CalculateOrderQuantity(self, symbol, target):
        """
        CalculateOrderQuantity(self: QCAlgorithm, symbol: Symbol, target: float) -> Decimal

        

            Calculate the order quantity to achieve 

             target-percent holdings.

        

        

            symbol: Security object we're asking for

            target: Target percentag holdings

            Returns: Order quantity to achieve this percentage

        CalculateOrderQuantity(self: QCAlgorithm, symbol: Symbol, target: Decimal) -> Decimal

        

            Calculate the order quantity to achieve 

             target-percent holdings.

        

        

            symbol: Security object we're asking for

            target: Target percentage holdings, this is an unlevered 

             value, so

                    if you have 2x leverage 

             and request 100% holdings, it will utilize half 

             of the

                    available margin

        

            Returns: Order quantity to achieve this percentage
        """
        pass

    def CC(self, symbol, shortRocPeriod, longRocPeriod, lwmaPeriod, resolution, selector):
        """ CC(self: QCAlgorithm, symbol: Symbol, shortRocPeriod: int, longRocPeriod: int, lwmaPeriod: int, resolution: Nullable[Resolution], selector: Func[IBaseData, Decimal]) -> CoppockCurve """
        pass

    def CCI(self, symbol, period, movingAverageType, resolution, selector):
        """ CCI(self: QCAlgorithm, symbol: Symbol, period: int, movingAverageType: MovingAverageType, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> CommodityChannelIndex """
        pass

    def CMO(self, symbol, period, resolution, selector):
        """ CMO(self: QCAlgorithm, symbol: Symbol, period: int, resolution: Nullable[Resolution], selector: Func[IBaseData, Decimal]) -> ChandeMomentumOscillator """
        pass

    def Consolidate(self, symbol, *__args):
        """
        Consolidate(self: QCAlgorithm, symbol: Symbol, period: Resolution, handler: Action[TradeBar]) -> IDataConsolidator

        Consolidate(self: QCAlgorithm, symbol: Symbol, period: TimeSpan, handler: Action[TradeBar]) -> IDataConsolidator

        Consolidate(self: QCAlgorithm, symbol: Symbol, period: Resolution, handler: Action[QuoteBar]) -> IDataConsolidator

        Consolidate(self: QCAlgorithm, symbol: Symbol, period: TimeSpan, handler: Action[QuoteBar]) -> IDataConsolidator

        Consolidate[T](self: QCAlgorithm, symbol: Symbol, period: TimeSpan, handler: Action[T]) -> IDataConsolidator

        Consolidate[T](self: QCAlgorithm, symbol: Symbol, period: Resolution, tickType: Nullable[TickType], handler: Action[T]) -> IDataConsolidator

        Consolidate[T](self: QCAlgorithm, symbol: Symbol, period: TimeSpan, tickType: Nullable[TickType], handler: Action[T]) -> IDataConsolidator

        Consolidate(self: QCAlgorithm, symbol: Symbol, calendar: Func[DateTime, CalendarInfo], handler: Action[QuoteBar]) -> IDataConsolidator

        Consolidate(self: QCAlgorithm, symbol: Symbol, calendar: Func[DateTime, CalendarInfo], handler: Action[TradeBar]) -> IDataConsolidator

        Consolidate[T](self: QCAlgorithm, symbol: Symbol, calendar: Func[DateTime, CalendarInfo], handler: Action[T]) -> IDataConsolidator

        Consolidate(self: QCAlgorithm, symbol: Symbol, period: Resolution, handler: PyObject) -> IDataConsolidator

        

            Registers the handler to receive consolidated 

             data for the specified symbol

        

        

            symbol: The symbol who's data is to be consolidated

            period: The consolidation period

            handler: Data handler receives new consolidated data when 

             generated

        

            Returns: A new consolidator matching the requested 

             parameters with the handler already registered

        

        Consolidate(self: QCAlgorithm, symbol: Symbol, period: Resolution, tickType: Nullable[TickType], handler: PyObject) -> IDataConsolidator

        Consolidate(self: QCAlgorithm, symbol: Symbol, period: TimeSpan, handler: PyObject) -> IDataConsolidator

        

            Registers the handler to receive consolidated 

             data for the specified symbol

        

        

            symbol: The symbol who's data is to be consolidated

            period: The consolidation period

            handler: Data handler receives new consolidated data when 

             generated

        

            Returns: A new consolidator matching the requested 

             parameters with the handler already registered

        

        Consolidate(self: QCAlgorithm, symbol: Symbol, period: TimeSpan, tickType: Nullable[TickType], handler: PyObject) -> IDataConsolidator

        Consolidate(self: QCAlgorithm, symbol: Symbol, calendar: Func[DateTime, CalendarInfo], handler: PyObject) -> IDataConsolidator
        """
        pass

    @staticmethod
    def CreateConsolidator(period, consolidatorInputType, tickType):
        """ CreateConsolidator(period: TimeSpan, consolidatorInputType: Type, tickType: Nullable[TickType]) -> IDataConsolidator """
        pass

    def CreateIndicatorName(self, symbol, type, resolution):
        """
        CreateIndicatorName(self: QCAlgorithm, symbol: Symbol, type: FormattableString, resolution: Nullable[Resolution]) -> str

        CreateIndicatorName(self: QCAlgorithm, symbol: Symbol, type: str, resolution: Nullable[Resolution]) -> str
        """
        pass

    def DCH(self, symbol, *__args):
        """
        DCH(self: QCAlgorithm, symbol: Symbol, upperPeriod: int, lowerPeriod: int, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> DonchianChannel

        DCH(self: QCAlgorithm, symbol: Symbol, period: int, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> DonchianChannel
        """
        pass

    def Debug(self, message):
        """
        Debug(self: QCAlgorithm, message: PyObject)

            Send a debug message to the web console:

        

            message: Message to send to debug console

        Debug(self: QCAlgorithm, message: str)

            Send a debug message to the web console:

        

            message: Message to send to debug console

        Debug(self: QCAlgorithm, message: int)

            Send a debug message to the web console:

        

            message: Message to send to debug console

        Debug(self: QCAlgorithm, message: float)

            Send a debug message to the web console:

        

            message: Message to send to debug console

        Debug(self: QCAlgorithm, message: Decimal)

            Send a debug message to the web console:

        

            message: Message to send to debug console
        """
        pass

    def DEMA(self, symbol, period, resolution, selector):
        """ DEMA(self: QCAlgorithm, symbol: Symbol, period: int, resolution: Nullable[Resolution], selector: Func[IBaseData, Decimal]) -> DoubleExponentialMovingAverage """
        pass

    def Download(self, address, headers=None, userName=None, password=None):
        """
        Download(self: QCAlgorithm, address: str, headers: PyObject) -> str

        

            Downloads the requested resource as a 

             System.String.

                    The resource to 

             download is specified as a System.String 

             containing the URI.

        

        

            address: A string containing the URI to download

            headers: Defines header values to add to the request

            Returns: The requested resource as a System.String

        Download(self: QCAlgorithm, address: str, headers: PyObject, userName: str, password: str) -> str

        

            Downloads the requested resource as a 

             System.String.

                    The resource to 

             download is specified as a System.String 

             containing the URI.

        

        

            address: A string containing the URI to download

            headers: Defines header values to add to the request

            userName: The user name associated with the credentials

            password: The password for the user name associated with 

             the credentials

        

            Returns: The requested resource as a System.String

        Download(self: QCAlgorithm, address: str) -> str

        

            Downloads the requested resource as a 

             System.String.

                    The resource to 

             download is specified as a System.String 

             containing the URI.

        

        

            address: A string containing the URI to download

            Returns: The requested resource as a System.String

        Download(self: QCAlgorithm, address: str, headers: IEnumerable[KeyValuePair[str, str]]) -> str

        Download(self: QCAlgorithm, address: str, headers: IEnumerable[KeyValuePair[str, str]], userName: str, password: str) -> str
        """
        pass

    def DPO(self, symbol, period, resolution, selector):
        """ DPO(self: QCAlgorithm, symbol: Symbol, period: int, resolution: Nullable[Resolution], selector: Func[IBaseData, Decimal]) -> DetrendedPriceOscillator """
        pass

    def EMA(self, symbol, period, *__args):
        """
        EMA(self: QCAlgorithm, symbol: Symbol, period: int, resolution: Nullable[Resolution], selector: Func[IBaseData, Decimal]) -> ExponentialMovingAverage

        EMA(self: QCAlgorithm, symbol: Symbol, period: int, smoothingFactor: Decimal, resolution: Nullable[Resolution], selector: Func[IBaseData, Decimal]) -> ExponentialMovingAverage
        """
        pass

    def EmitInsights(self, *__args):
        """
        EmitInsights(self: QCAlgorithm, *insights: Array[Insight])

            Manually emit insights from an algorithm.

               

                  This is typically invoked before calls to 

             submit orders in algorithms written against

             

                    QCAlgorithm that have been ported into the 

             algorithm framework.

        

        

            insights: The array of insights to be emitted

        EmitInsights(self: QCAlgorithm, insight: Insight)

            Manually emit insights from an algorithm.

               

                  This is typically invoked before calls to 

             submit orders in algorithms written against

             

                    QCAlgorithm that have been ported into the 

             algorithm framework.

        

        

            insight: The insight to be emitted
        """
        pass

    def Error(self, *__args):
        """
        Error(self: QCAlgorithm, message: PyObject)

            Send a string error message to the Console.

        

            message: Message to display in errors grid

        Error(self: QCAlgorithm, message: str)

            Send a string error message to the Console.

        

            message: Message to display in errors grid

        Error(self: QCAlgorithm, message: int)

            Send a int error message to the Console.

        

            message: Message to display in errors grid

        Error(self: QCAlgorithm, message: float)

            Send a double error message to the Console.

        

            message: Message to display in errors grid

        Error(self: QCAlgorithm, message: Decimal)

            Send a decimal error message to the Console.

        

            message: Message to display in errors grid

        Error(self: QCAlgorithm, error: Exception)

            Send a string error message to the Console.

        

            error: Exception object captured from a try catch loop
        """
        pass

    def ExerciseOption(self, optionSymbol, quantity, asynchronous, tag):
        """
        ExerciseOption(self: QCAlgorithm, optionSymbol: Symbol, quantity: int, asynchronous: bool, tag: str) -> OrderTicket

        

            Send an exercise order to the transaction handler

        

            optionSymbol: String symbol for the option position

            quantity: Quantity of options contracts

            asynchronous: Send the order asynchrously (false). Otherwise 

             we'll block until it fills

        

            tag: String tag for the order (optional)
        """
        pass

    def FilteredIdentity(self, symbol, *__args):
        """
        FilteredIdentity(self: QCAlgorithm, symbol: Symbol, selector: Func[IBaseData, IBaseDataBar], filter: Func[IBaseData, bool], fieldName: str) -> FilteredIdentity

        FilteredIdentity(self: QCAlgorithm, symbol: Symbol, resolution: Resolution, selector: Func[IBaseData, IBaseDataBar], filter: Func[IBaseData, bool], fieldName: str) -> FilteredIdentity

        FilteredIdentity(self: QCAlgorithm, symbol: Symbol, resolution: TimeSpan, selector: Func[IBaseData, IBaseDataBar], filter: Func[IBaseData, bool], fieldName: str) -> FilteredIdentity

        FilteredIdentity(self: QCAlgorithm, symbol: Symbol, selector: PyObject, filter: PyObject, fieldName: str) -> FilteredIdentity

        

            Creates a new FilteredIdentity indicator for the 

             symbol The indicator will be automatically

              

                   updated on the symbol's subscription 

             resolution

        

        

            symbol: The symbol whose values we want as an indicator

            selector: Selects a value from the BaseData, if null 

             defaults to the .Value property (x => x.Value)

        

            filter: Filters the IBaseData send into the indicator, if 

             null defaults to true (x => true) which means no 

             filter

        

            fieldName: The name of the field being selected

            Returns: A new FilteredIdentity indicator for the 

             specified symbol and selector

        

        FilteredIdentity(self: QCAlgorithm, symbol: Symbol, resolution: Resolution, selector: PyObject, filter: PyObject, fieldName: str) -> FilteredIdentity

        

            Creates a new FilteredIdentity indicator for the 

             symbol The indicator will be automatically

              

                   updated on the symbol's subscription 

             resolution

        

        

            symbol: The symbol whose values we want as an indicator

            resolution: The desired resolution of the data

            selector: Selects a value from the BaseData, if null 

             defaults to the .Value property (x => x.Value)

        

            filter: Filters the IBaseData send into the indicator, if 

             null defaults to true (x => true) which means no 

             filter

        

            fieldName: The name of the field being selected

            Returns: A new FilteredIdentity indicator for the 

             specified symbol and selector

        

        FilteredIdentity(self: QCAlgorithm, symbol: Symbol, resolution: TimeSpan, selector: PyObject, filter: PyObject, fieldName: str) -> FilteredIdentity

        

            Creates a new FilteredIdentity indicator for the 

             symbol The indicator will be automatically

              

                   updated on the symbol's subscription 

             resolution

        

        

            symbol: The symbol whose values we want as an indicator

            resolution: The desired resolution of the data

            selector: Selects a value from the BaseData, if null 

             defaults to the .Value property (x => x.Value)

        

            filter: Filters the IBaseData send into the indicator, if 

             null defaults to true (x => true) which means no 

             filter

        

            fieldName: The name of the field being selected

            Returns: A new FilteredIdentity indicator for the 

             specified symbol and selector
        """
        pass

    def FISH(self, symbol, period, resolution, selector):
        """ FISH(self: QCAlgorithm, symbol: Symbol, period: int, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> FisherTransform """
        pass

    def FRAMA(self, symbol, period, longPeriod, resolution, selector):
        """ FRAMA(self: QCAlgorithm, symbol: Symbol, period: int, longPeriod: int, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> FractalAdaptiveMovingAverage """
        pass

    def FrameworkPostInitialize(self):
        """
        FrameworkPostInitialize(self: QCAlgorithm)

            Called by setup handlers after Initialize and 

             allows the algorithm a chance to organize

               

                  the data gather in the Initialize method
        """
        pass

    def GetChartUpdates(self, clearChartData):
        """
        GetChartUpdates(self: QCAlgorithm, clearChartData: bool) -> List[Chart]

        

            Get the chart updates by fetch the recent points 

             added and return for dynamic plotting.

        

            Returns: List of chart updates since the last request
        """
        pass

    def GetLastKnownPrice(self, security):
        """
        GetLastKnownPrice(self: QCAlgorithm, security: Security) -> BaseData

        

            Get the last known price using the history 

             provider.

                    Useful for seeding 

             securities with the correct price

        

        

            security: QuantConnect.Securities.Security object for which 

             to retrieve historical data

        

            Returns: A single QuantConnect.Data.BaseData object with 

             the last known price
        """
        pass

    def GetLocked(self):
        """
        GetLocked(self: QCAlgorithm) -> bool

        

            Gets whether or not this algorithm has been 

             locked and fully initialized
        """
        pass

    def GetParameter(self, name):
        """
        GetParameter(self: QCAlgorithm, name: str) -> str

        

            Gets the parameter with the specified name. If a 

             parameter

                    with the specified name 

             does not exist, null is returned

        

        

            name: The name of the parameter to get

            Returns: The value of the specified parameter, or null if 

             not found
        """
        pass

    def GetParameters(self):
        """
        GetParameters(self: QCAlgorithm) -> IReadOnlyDictionary[str, str]

        

            Gets a read-only dictionary with all current 

             parameters
        """
        pass

    def GetWarmupHistoryRequests(self):
        """
        GetWarmupHistoryRequests(self: QCAlgorithm) -> IEnumerable[HistoryRequest]

        

            Gets the history requests required for provide 

             warm up data for the algorithm
        """
        pass

    def HeikinAshi(self, symbol, resolution, selector):
        """ HeikinAshi(self: QCAlgorithm, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, TradeBar]) -> HeikinAshi """
        pass

    def History(self, *__args):
        """
        History(self: QCAlgorithm, span: TimeSpan, resolution: Nullable[Resolution]) -> IEnumerable[Slice]

        History(self: QCAlgorithm, type: PyObject, symbol: Symbol, start: DateTime, end: DateTime, resolution: Nullable[Resolution]) -> PyObject

        History(self: QCAlgorithm, type: PyObject, tickers: PyObject, span: TimeSpan, resolution: Nullable[Resolution]) -> PyObject

        History(self: QCAlgorithm, type: PyObject, tickers: PyObject, periods: int, resolution: Nullable[Resolution]) -> PyObject

        History(self: QCAlgorithm, type: PyObject, tickers: PyObject, start: DateTime, end: DateTime, resolution: Nullable[Resolution]) -> PyObject

        History(self: QCAlgorithm, tickers: PyObject, start: DateTime, end: DateTime, resolution: Nullable[Resolution]) -> PyObject

        History(self: QCAlgorithm, tickers: PyObject, span: TimeSpan, resolution: Nullable[Resolution]) -> PyObject

        History(self: QCAlgorithm, tickers: PyObject, periods: int, resolution: Nullable[Resolution]) -> PyObject

        History(self: QCAlgorithm, requests: IEnumerable[HistoryRequest]) -> IEnumerable[Slice]

        History(self: QCAlgorithm, request: HistoryRequest) -> IEnumerable[Slice]

        

            Executes the specified history request

        

            request: the history request to execute

            Returns: An enumerable of slice satisfying the specified 

             history request

        

        History(self: QCAlgorithm, symbols: IEnumerable[Symbol], start: DateTime, end: DateTime, resolution: Nullable[Resolution], fillForward: Nullable[bool], extendedMarket: Nullable[bool]) -> IEnumerable[Slice]

        History(self: QCAlgorithm, symbols: IEnumerable[Symbol], periods: int, resolution: Nullable[Resolution]) -> IEnumerable[Slice]

        History(self: QCAlgorithm, symbols: IEnumerable[Symbol], span: TimeSpan, resolution: Nullable[Resolution]) -> IEnumerable[Slice]

        History(self: QCAlgorithm, symbol: Symbol, start: DateTime, end: DateTime, resolution: Nullable[Resolution]) -> IEnumerable[TradeBar]

        History(self: QCAlgorithm, symbol: Symbol, span: TimeSpan, resolution: Nullable[Resolution]) -> IEnumerable[TradeBar]

        History[T](self: QCAlgorithm, symbol: Symbol, start: DateTime, end: DateTime, resolution: Nullable[Resolution]) -> IEnumerable[T]

        History[T](self: QCAlgorithm, symbol: Symbol, periods: int, resolution: Nullable[Resolution]) -> IEnumerable[T]

        History(self: QCAlgorithm, symbol: Symbol, periods: int, resolution: Nullable[Resolution]) -> IEnumerable[TradeBar]

        History[T](self: QCAlgorithm, symbol: Symbol, span: TimeSpan, resolution: Nullable[Resolution]) -> IEnumerable[T]

        History[T](self: QCAlgorithm, symbols: IEnumerable[Symbol], start: DateTime, end: DateTime, resolution: Nullable[Resolution]) -> IEnumerable[DataDictionary[T]]

        History[T](self: QCAlgorithm, symbols: IEnumerable[Symbol], periods: int, resolution: Nullable[Resolution]) -> IEnumerable[DataDictionary[T]]

        History[T](self: QCAlgorithm, symbols: IEnumerable[Symbol], span: TimeSpan, resolution: Nullable[Resolution]) -> IEnumerable[DataDictionary[T]]

        History[T](self: QCAlgorithm, span: TimeSpan, resolution: Nullable[Resolution]) -> IEnumerable[DataDictionary[T]]

        History(self: QCAlgorithm, periods: int, resolution: Nullable[Resolution]) -> IEnumerable[Slice]

        History(self: QCAlgorithm, type: PyObject, symbol: Symbol, periods: int, resolution: Nullable[Resolution]) -> PyObject

        History(self: QCAlgorithm, type: PyObject, symbol: Symbol, span: TimeSpan, resolution: Nullable[Resolution]) -> PyObject
        """
        pass

    def HMA(self, symbol, period, resolution, selector):
        """ HMA(self: QCAlgorithm, symbol: Symbol, period: int, resolution: Nullable[Resolution], selector: Func[IBaseData, Decimal]) -> HullMovingAverage """
        pass

    def ICHIMOKU(self, symbol, tenkanPeriod, kijunPeriod, senkouAPeriod, senkouBPeriod, senkouADelayPeriod, senkouBDelayPeriod, resolution):
        """ ICHIMOKU(self: QCAlgorithm, symbol: Symbol, tenkanPeriod: int, kijunPeriod: int, senkouAPeriod: int, senkouBPeriod: int, senkouADelayPeriod: int, senkouBDelayPeriod: int, resolution: Nullable[Resolution]) -> IchimokuKinkoHyo """
        pass

    def Identity(self, symbol, *__args):
        """
        Identity(self: QCAlgorithm, symbol: Symbol, selector: Func[IBaseData, Decimal], fieldName: str) -> Identity

        Identity(self: QCAlgorithm, symbol: Symbol, resolution: Resolution, selector: Func[IBaseData, Decimal], fieldName: str) -> Identity

        Identity(self: QCAlgorithm, symbol: Symbol, resolution: TimeSpan, selector: Func[IBaseData, Decimal], fieldName: str) -> Identity
        """
        pass

    def Initialize(self):
        """
        Initialize(self: QCAlgorithm)

            Initialise the data and resolution required, as 

             well as the cash and start-end dates for your 

             algorithm. All algorithms must initialized.
        """
        pass

    def IsMarketOpen(self, symbol):
        """
        IsMarketOpen(self: QCAlgorithm, symbol: Symbol) -> bool

        

            Determines if the exchange for the specified 

             symbol is open at the current time.

        

        

            symbol: The symbol

            Returns: True if the exchange is considered open at the 

             current time, false otherwise
        """
        pass

    def KAMA(self, symbol, period, *__args):
        """
        KAMA(self: QCAlgorithm, symbol: Symbol, period: int, resolution: Nullable[Resolution], selector: Func[IBaseData, Decimal]) -> KaufmanAdaptiveMovingAverage

        KAMA(self: QCAlgorithm, symbol: Symbol, period: int, fastEmaPeriod: int, slowEmaPeriod: int, resolution: Nullable[Resolution], selector: Func[IBaseData, Decimal]) -> KaufmanAdaptiveMovingAverage
        """
        pass

    def KCH(self, symbol, period, k, movingAverageType, resolution, selector):
        """ KCH(self: QCAlgorithm, symbol: Symbol, period: int, k: Decimal, movingAverageType: MovingAverageType, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> KeltnerChannels """
        pass

    def LimitOrder(self, symbol, quantity, limitPrice, tag):
        """
        LimitOrder(self: QCAlgorithm, symbol: Symbol, quantity: int, limitPrice: Decimal, tag: str) -> OrderTicket

        

            Send a limit order to the transaction handler:

        

            symbol: String symbol for the asset

            quantity: Quantity of shares for limit order

            limitPrice: Limit price to fill this order

            tag: String tag for the order (optional)

            Returns: Order id

        LimitOrder(self: QCAlgorithm, symbol: Symbol, quantity: float, limitPrice: Decimal, tag: str) -> OrderTicket

        

            Send a limit order to the transaction handler:

        

            symbol: String symbol for the asset

            quantity: Quantity of shares for limit order

            limitPrice: Limit price to fill this order

            tag: String tag for the order (optional)

            Returns: Order id

        LimitOrder(self: QCAlgorithm, symbol: Symbol, quantity: Decimal, limitPrice: Decimal, tag: str) -> OrderTicket

        

            Send a limit order to the transaction handler:

        

            symbol: String symbol for the asset

            quantity: Quantity of shares for limit order

            limitPrice: Limit price to fill this order

            tag: String tag for the order (optional)

            Returns: Order id
        """
        pass

    def Liquidate(self, symbolToLiquidate, tag):
        """
        Liquidate(self: QCAlgorithm, symbolToLiquidate: Symbol, tag: str) -> List[int]

        

            Liquidate all holdings and cancel open orders. 

             Called at the end of day for tick-strategies.

        

        

            symbolToLiquidate: Symbols we wish to liquidate

            tag: Custom tag to know who is calling this.

            Returns: Array of order ids for liquidated symbols
        """
        pass

    def Log(self, message):
        """
        Log(self: QCAlgorithm, message: PyObject)

            Added another method for logging if user guessed.

        

            message: String message to log.

        Log(self: QCAlgorithm, message: str)

            Added another method for logging if user guessed.

        

            message: String message to log.

        Log(self: QCAlgorithm, message: int)

            Added another method for logging if user guessed.

        

            message: Int message to log.

        Log(self: QCAlgorithm, message: float)

            Added another method for logging if user guessed.

        

            message: Double message to log.

        Log(self: QCAlgorithm, message: Decimal)

            Added another method for logging if user guessed.

        

            message: Decimal message to log.
        """
        pass

    def LOGR(self, symbol, period, resolution, selector):
        """ LOGR(self: QCAlgorithm, symbol: Symbol, period: int, resolution: Nullable[Resolution], selector: Func[IBaseData, Decimal]) -> LogReturn """
        pass

    def LSMA(self, symbol, period, resolution, selector):
        """ LSMA(self: QCAlgorithm, symbol: Symbol, period: int, resolution: Nullable[Resolution], selector: Func[IBaseData, Decimal]) -> LeastSquaresMovingAverage """
        pass

    def LWMA(self, symbol, period, resolution, selector):
        """ LWMA(self: QCAlgorithm, symbol: Symbol, period: int, resolution: Nullable[Resolution], selector: Func[IBaseData, Decimal]) -> LinearWeightedMovingAverage """
        pass

    def MACD(self, symbol, fastPeriod, slowPeriod, signalPeriod, type, resolution, selector):
        """ MACD(self: QCAlgorithm, symbol: Symbol, fastPeriod: int, slowPeriod: int, signalPeriod: int, type: MovingAverageType, resolution: Nullable[Resolution], selector: Func[IBaseData, Decimal]) -> MovingAverageConvergenceDivergence """
        pass

    def MAD(self, symbol, period, resolution, selector):
        """ MAD(self: QCAlgorithm, symbol: Symbol, period: int, resolution: Nullable[Resolution], selector: Func[IBaseData, Decimal]) -> MeanAbsoluteDeviation """
        pass

    def MarketOnCloseOrder(self, symbol, quantity, tag):
        """
        MarketOnCloseOrder(self: QCAlgorithm, symbol: Symbol, quantity: int, tag: str) -> OrderTicket

        

            Market on close order implementation: Send a 

             market order when the exchange closes

        

        

            symbol: The symbol to be ordered

            quantity: The number of shares to required

            tag: Place a custom order property or tag (e.g. 

             indicator data).

        

            Returns: The order ID

        MarketOnCloseOrder(self: QCAlgorithm, symbol: Symbol, quantity: float, tag: str) -> OrderTicket

        

            Market on close order implementation: Send a 

             market order when the exchange closes

        

        

            symbol: The symbol to be ordered

            quantity: The number of shares to required

            tag: Place a custom order property or tag (e.g. 

             indicator data).

        

            Returns: The order ID

        MarketOnCloseOrder(self: QCAlgorithm, symbol: Symbol, quantity: Decimal, tag: str) -> OrderTicket

        

            Market on close order implementation: Send a 

             market order when the exchange closes

        

        

            symbol: The symbol to be ordered

            quantity: The number of shares to required

            tag: Place a custom order property or tag (e.g. 

             indicator data).

        

            Returns: The order ID
        """
        pass

    def MarketOnOpenOrder(self, symbol, quantity, tag):
        """
        MarketOnOpenOrder(self: QCAlgorithm, symbol: Symbol, quantity: float, tag: str) -> OrderTicket

        

            Market on open order implementation: Send a 

             market order when the exchange opens

        

        

            symbol: The symbol to be ordered

            quantity: The number of shares to required

            tag: Place a custom order property or tag (e.g. 

             indicator data).

        

            Returns: The order ID

        MarketOnOpenOrder(self: QCAlgorithm, symbol: Symbol, quantity: int, tag: str) -> OrderTicket

        

            Market on open order implementation: Send a 

             market order when the exchange opens

        

        

            symbol: The symbol to be ordered

            quantity: The number of shares to required

            tag: Place a custom order property or tag (e.g. 

             indicator data).

        

            Returns: The order ID

        MarketOnOpenOrder(self: QCAlgorithm, symbol: Symbol, quantity: Decimal, tag: str) -> OrderTicket

        

            Market on open order implementation: Send a 

             market order when the exchange opens

        

        

            symbol: The symbol to be ordered

            quantity: The number of shares to required

            tag: Place a custom order property or tag (e.g. 

             indicator data).

        

            Returns: The order ID
        """
        pass

    def MarketOrder(self, symbol, quantity, asynchronous, tag):
        """
        MarketOrder(self: QCAlgorithm, symbol: Symbol, quantity: int, asynchronous: bool, tag: str) -> OrderTicket

        

            Market order implementation: Send a market order 

             and wait for it to be filled.

        

        

            symbol: Symbol of the MarketType Required.

            quantity: Number of shares to request.

            asynchronous: Send the order asynchrously (false). Otherwise 

             we'll block until it fills

        

            tag: Place a custom order property or tag (e.g. 

             indicator data).

        

            Returns: int Order id

        MarketOrder(self: QCAlgorithm, symbol: Symbol, quantity: float, asynchronous: bool, tag: str) -> OrderTicket

        

            Market order implementation: Send a market order 

             and wait for it to be filled.

        

        

            symbol: Symbol of the MarketType Required.

            quantity: Number of shares to request.

            asynchronous: Send the order asynchrously (false). Otherwise 

             we'll block until it fills

        

            tag: Place a custom order property or tag (e.g. 

             indicator data).

        

            Returns: int Order id

        MarketOrder(self: QCAlgorithm, symbol: Symbol, quantity: Decimal, asynchronous: bool, tag: str) -> OrderTicket

        

            Market order implementation: Send a market order 

             and wait for it to be filled.

        

        

            symbol: Symbol of the MarketType Required.

            quantity: Number of shares to request.

            asynchronous: Send the order asynchrously (false). Otherwise 

             we'll block until it fills

        

            tag: Place a custom order property or tag (e.g. 

             indicator data).

        

            Returns: int Order id
        """
        pass

    def MASS(self, symbol, emaPeriod, sumPeriod, resolution, selector):
        """ MASS(self: QCAlgorithm, symbol: Symbol, emaPeriod: int, sumPeriod: int, resolution: Nullable[Resolution], selector: Func[IBaseData, TradeBar]) -> MassIndex """
        pass

    def MAX(self, symbol, period, resolution, selector):
        """ MAX(self: QCAlgorithm, symbol: Symbol, period: int, resolution: Nullable[Resolution], selector: Func[IBaseData, Decimal]) -> Maximum """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject

        

            Creates a shallow copy of the current 

             System.MarshalByRefObject object.

        

        

            cloneIdentity: false to delete the current 

             System.MarshalByRefObject object's identity, 

             which will cause the object to be assigned a new 

             identity when it is marshaled across a remoting 

             boundary. A value of false is usually 

             appropriate. true to copy the current 

             System.MarshalByRefObject object's identity to 

             its clone, which will cause remoting client calls 

             to be routed to the remote server object.

        

            Returns: A shallow copy of the current 

             System.MarshalByRefObject object.

        

        MemberwiseClone(self: object) -> object

        

            Creates a shallow copy of the current 

             System.Object.

        

            Returns: A shallow copy of the current System.Object.
        """
        pass

    def MFI(self, symbol, period, resolution, selector):
        """ MFI(self: QCAlgorithm, symbol: Symbol, period: int, resolution: Nullable[Resolution], selector: Func[IBaseData, TradeBar]) -> MoneyFlowIndex """
        pass

    def MIDPOINT(self, symbol, period, resolution, selector):
        """ MIDPOINT(self: QCAlgorithm, symbol: Symbol, period: int, resolution: Nullable[Resolution], selector: Func[IBaseData, Decimal]) -> MidPoint """
        pass

    def MIDPRICE(self, symbol, period, resolution, selector):
        """ MIDPRICE(self: QCAlgorithm, symbol: Symbol, period: int, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> MidPrice """
        pass

    def MIN(self, symbol, period, resolution, selector):
        """ MIN(self: QCAlgorithm, symbol: Symbol, period: int, resolution: Nullable[Resolution], selector: Func[IBaseData, Decimal]) -> Minimum """
        pass

    def MOM(self, symbol, period, resolution, selector):
        """ MOM(self: QCAlgorithm, symbol: Symbol, period: int, resolution: Nullable[Resolution], selector: Func[IBaseData, Decimal]) -> Momentum """
        pass

    def MOMERSION(self, symbol, minPeriod, fullPeriod, resolution, selector):
        """ MOMERSION(self: QCAlgorithm, symbol: Symbol, minPeriod: Nullable[int], fullPeriod: int, resolution: Nullable[Resolution], selector: Func[IBaseData, Decimal]) -> MomersionIndicator """
        pass

    def MOMP(self, symbol, period, resolution, selector):
        """ MOMP(self: QCAlgorithm, symbol: Symbol, period: int, resolution: Nullable[Resolution], selector: Func[IBaseData, Decimal]) -> MomentumPercent """
        pass

    def NATR(self, symbol, period, resolution, selector):
        """ NATR(self: QCAlgorithm, symbol: Symbol, period: int, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> NormalizedAverageTrueRange """
        pass

    def OBV(self, symbol, resolution, selector):
        """ OBV(self: QCAlgorithm, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, TradeBar]) -> OnBalanceVolume """
        pass

    def OnAssignmentOrderEvent(self, assignmentEvent):
        """
        OnAssignmentOrderEvent(self: QCAlgorithm, assignmentEvent: OrderEvent)

            Option assignment event handler. On an option 

             assignment event for short legs the resulting 

             information is passed to this method.

        

        

            assignmentEvent: Option exercise event details containing details 

             of the assignment
        """
        pass

    def OnBrokerageDisconnect(self):
        """
        OnBrokerageDisconnect(self: QCAlgorithm)

            Brokerage disconnected event handler. This method 

             is called when the brokerage connection is lost.
        """
        pass

    def OnBrokerageMessage(self, messageEvent):
        """
        OnBrokerageMessage(self: QCAlgorithm, messageEvent: BrokerageMessageEvent)

            Brokerage message event handler. This method is 

             called for all types of brokerage messages.
        """
        pass

    def OnBrokerageReconnect(self):
        """
        OnBrokerageReconnect(self: QCAlgorithm)

            Brokerage reconnected event handler. This method 

             is called when the brokerage connection is 

             restored after a disconnection.
        """
        pass

    def OnData(self, slice):
        """
        OnData(self: QCAlgorithm, slice: Slice)

            Event - v3.0 DATA EVENT HANDLER: (Pattern) Basic 

             template for user to override for receiving all 

             subscription data in a single event

        

        

            slice: The current slice of data keyed by symbol string
        """
        pass

    def OnEndOfAlgorithm(self):
        """
        OnEndOfAlgorithm(self: QCAlgorithm)

            End of algorithm run event handler. This method 

             is called at the end of a backtest or live 

             trading operation. Intended for closing out logs.
        """
        pass

    def OnEndOfDay(self, symbol=None):
        """
        OnEndOfDay(self: QCAlgorithm)

            End of a trading day event handler. This method 

             is called at the end of the algorithm day (or 

             multiple times if trading multiple assets).

        

        OnEndOfDay(self: QCAlgorithm, symbol: str)

            End of a trading day event handler. This method 

             is called at the end of the algorithm day (or 

             multiple times if trading multiple assets).

        

        

            symbol: Asset symbol for this end of day event. Forex and 

             equities have different closing hours.

        

        OnEndOfDay(self: QCAlgorithm, symbol: Symbol)

            End of a trading day event handler. This method 

             is called at the end of the algorithm day (or 

             multiple times if trading multiple assets).

        

        

            symbol: Asset symbol for this end of day event. Forex and 

             equities have different closing hours.
        """
        pass

    def OnEndOfTimeStep(self):
        """
        OnEndOfTimeStep(self: QCAlgorithm)

            Invoked at the end of every time step. This 

             allows the algorithm

                    to process 

             events before advancing to the next time step.
        """
        pass

    def OnFrameworkData(self, slice):
        """
        OnFrameworkData(self: QCAlgorithm, slice: Slice)

            Used to send data updates to algorithm framework 

             models

        

        

            slice: The current data slice
        """
        pass

    def OnFrameworkSecuritiesChanged(self, changes):
        """
        OnFrameworkSecuritiesChanged(self: QCAlgorithm, changes: SecurityChanges)

            Used to send security changes to algorithm 

             framework models

        

        

            changes: Security additions/removals for this time step
        """
        pass

    def OnMarginCall(self, requests):
        """ OnMarginCall(self: QCAlgorithm, requests: List[SubmitOrderRequest]) """
        pass

    def OnMarginCallWarning(self):
        """
        OnMarginCallWarning(self: QCAlgorithm)

            Margin call warning event handler. This method is 

             called when Portfolio.MarginRemaining is under 5% 

             of your Portfolio.TotalPortfolioValue
        """
        pass

    def OnOrderEvent(self, orderEvent):
        """
        OnOrderEvent(self: QCAlgorithm, orderEvent: OrderEvent)

            Order fill event handler. On an order fill update 

             the resulting information is passed to this 

             method.

        

        

            orderEvent: Order event details containing details of the 

             evemts
        """
        pass

    def OnSecuritiesChanged(self, changes):
        """
        OnSecuritiesChanged(self: QCAlgorithm, changes: SecurityChanges)

            Event fired each time the we add/remove 

             securities from the data feed

        

        

            changes: Security additions/removals for this time step
        """
        pass

    def OnWarmupFinished(self):
        """
        OnWarmupFinished(self: QCAlgorithm)

            Called when the algorithm has completed 

             initialization and warm up.
        """
        pass

    def Order(self, *__args):
        """
        Order(self: QCAlgorithm, symbol: Symbol, quantity: float) -> OrderTicket

        

            Issue an order/trade for asset: Alias wrapper for 

             Order(string, int);

        

        Order(self: QCAlgorithm, symbol: Symbol, quantity: int) -> OrderTicket

        

            Issue an order/trade for asset

        Order(self: QCAlgorithm, symbol: Symbol, quantity: Decimal) -> OrderTicket

        

            Issue an order/trade for asset

        Order(self: QCAlgorithm, symbol: Symbol, quantity: Decimal, asynchronous: bool, tag: str) -> OrderTicket

        

            Wrapper for market order method: submit a new 

             order for quantity of symbol using type order.

        

        

            symbol: Symbol of the MarketType Required.

            quantity: Number of shares to request.

            asynchronous: Send the order asynchrously (false). Otherwise 

             we'll block until it fills

        

            tag: Place a custom order property or tag (e.g. 

             indicator data).

        

        Order(self: QCAlgorithm, strategy: OptionStrategy, quantity: int) -> IEnumerable[OrderTicket]

        

            Issue an order/trade for buying/selling an option 

             strategy

        

        

            strategy: Specification of the strategy to trade

            quantity: Quantity of the strategy to trade

            Returns: Sequence of order ids

        Order(self: QCAlgorithm, symbol: Symbol, quantity: int, type: OrderType, asynchronous: bool, tag: str) -> OrderTicket

        

            Obsolete implementation of Order method accepting 

             a OrderType. This was deprecated since it

               

                  was impossible to generate other orders via 

             this method. Any calls to this method will always 

             default to a Market Order.

        

        

            symbol: Symbol we want to purchase

            quantity: Quantity to buy, + is long, - short.

            type: Order Type

            asynchronous: Don't wait for the response, just submit order 

             and move on.

        

            tag: Custom data for this order

            Returns: Integer Order ID.

        Order(self: QCAlgorithm, symbol: Symbol, quantity: Decimal, type: OrderType) -> OrderTicket

        

            Obsolete method for placing orders.

        Order(self: QCAlgorithm, symbol: Symbol, quantity: int, type: OrderType) -> OrderTicket

        

            Obsolete method for placing orders.
        """
        pass

    def Plot(self, *__args):
        """
        Plot(self: QCAlgorithm, series: str, value: Decimal)

            Plot a chart using string series name, with value.

        

            series: Name of the plot series

            value: Value to plot

        Plot(self: QCAlgorithm, series: str, value: float)

            Plot a chart using string series name, with 

             double value.

        

        Plot(self: QCAlgorithm, series: str, value: int)

            Plot a chart using string series name, with int 

             value.

        

        Plot(self: QCAlgorithm, series: str, value: Single)

            Plot a chart using string series name, with float 

             value.

        

        Plot(self: QCAlgorithm, chart: str, series: str, value: float)

            Plot a chart to string chart name, using string 

             series name, with double value.

        

        Plot(self: QCAlgorithm, chart: str, series: str, value: int)

            Plot a chart to string chart name, using string 

             series name, with int value

        

        Plot(self: QCAlgorithm, chart: str, series: str, value: Single)

            Plot a chart to string chart name, using string 

             series name, with float value

        

        Plot(self: QCAlgorithm, chart: str, series: str, value: Decimal)

            Plot a value to a chart of string-chart name, 

             with string series name, and decimal value. If 

             chart does not exist, create it.

        

        

            chart: Chart name

            series: Series name

            value: Value of the point

        Plot[T](self: QCAlgorithm, chart: str, *indicators: Array[IndicatorBase[T]])Plot(self: QCAlgorithm, series: str, pyObject: PyObject)

            Plot a chart using string series name, with value.

        

            series: Name of the plot series

            pyObject: PyObject with the value to plot

        Plot(self: QCAlgorithm, chart: str, first: Indicator, second: Indicator, third: Indicator, fourth: Indicator)

            Plots the value of each indicator on the chart

        

            chart: The chart's name

            first: The first indicator to plot

            second: The second indicator to plot

            third: The third indicator to plot

            fourth: The fourth indicator to plot

        Plot(self: QCAlgorithm, chart: str, first: BarIndicator, second: BarIndicator, third: BarIndicator, fourth: BarIndicator)

            Plots the value of each indicator on the chart

        

            chart: The chart's name

            first: The first indicator to plot

            second: The second indicator to plot

            third: The third indicator to plot

            fourth: The fourth indicator to plot

        Plot(self: QCAlgorithm, chart: str, first: TradeBarIndicator, second: TradeBarIndicator, third: TradeBarIndicator, fourth: TradeBarIndicator)

            Plots the value of each indicator on the chart

        

            chart: The chart's name

            first: The first indicator to plot

            second: The second indicator to plot

            third: The third indicator to plot

            fourth: The fourth indicator to plot
        """
        pass

    def PlotIndicator(self, chart, *__args):
        """
        PlotIndicator[T](self: QCAlgorithm, chart: str, *indicators: Array[IndicatorBase[T]])PlotIndicator[T](self: QCAlgorithm, chart: str, waitForReady: bool, *indicators: Array[IndicatorBase[T]])PlotIndicator(self: QCAlgorithm, chart: str, first: PyObject, second: PyObject, third: PyObject, fourth: PyObject)

            Automatically plots each indicator when a new 

             value is available

        

        PlotIndicator(self: QCAlgorithm, chart: str, waitForReady: bool, first: PyObject, second: PyObject, third: PyObject, fourth: PyObject)

            Automatically plots each indicator when a new 

             value is available
        """
        pass

    def PostInitialize(self):
        """
        PostInitialize(self: QCAlgorithm)

            Called by setup handlers after Initialize and 

             allows the algorithm a chance to organize

               

                  the data gather in the Initialize method
        """
        pass

    def PPO(self, symbol, fastPeriod, slowPeriod, movingAverageType, resolution, selector):
        """ PPO(self: QCAlgorithm, symbol: Symbol, fastPeriod: int, slowPeriod: int, movingAverageType: MovingAverageType, resolution: Nullable[Resolution], selector: Func[IBaseData, Decimal]) -> PercentagePriceOscillator """
        pass

    def PSAR(self, symbol, afStart, afIncrement, afMax, resolution, selector):
        """ PSAR(self: QCAlgorithm, symbol: Symbol, afStart: Decimal, afIncrement: Decimal, afMax: Decimal, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> ParabolicStopAndReverse """
        pass

    def Quit(self, message):
        """
        Quit(self: QCAlgorithm, message: PyObject)

            Terminate the algorithm after processing the 

             current event handler.

        

        

            message: Exit message to display on quitting

        Quit(self: QCAlgorithm, message: str)

            Terminate the algorithm after processing the 

             current event handler.

        

        

            message: Exit message to display on quitting
        """
        pass

    def RC(self, symbol, period, k, resolution, selector):
        """ RC(self: QCAlgorithm, symbol: Symbol, period: int, k: Decimal, resolution: Nullable[Resolution], selector: Func[IBaseData, Decimal]) -> RegressionChannel """
        pass

    def Record(self, series, value):
        """
        Record(self: QCAlgorithm, series: str, value: int)

            Plot a chart using string series name, with int 

             value. Alias of Plot();

        

        Record(self: QCAlgorithm, series: str, value: float)

            Plot a chart using string series name, with 

             double value. Alias of Plot();

        

        Record(self: QCAlgorithm, series: str, value: Decimal)

            Plot a chart using string series name, with 

             decimal value. Alias of Plot();
        """
        pass

    def RegisterIndicator(self, symbol, indicator, *__args):
        """
        RegisterIndicator(self: QCAlgorithm, symbol: Symbol, indicator: IndicatorBase[IndicatorDataPoint], resolution: Nullable[Resolution], selector: Func[IBaseData, Decimal])RegisterIndicator(self: QCAlgorithm, symbol: Symbol, indicator: IndicatorBase[IndicatorDataPoint], resolution: Nullable[TimeSpan], selector: Func[IBaseData, Decimal])RegisterIndicator(self: QCAlgorithm, symbol: Symbol, indicator: IndicatorBase[IndicatorDataPoint], consolidator: IDataConsolidator, selector: Func[IBaseData, Decimal])RegisterIndicator[T](self: QCAlgorithm, symbol: Symbol, indicator: IndicatorBase[T], resolution: Nullable[Resolution])RegisterIndicator[T](self: QCAlgorithm, symbol: Symbol, indicator: IndicatorBase[T], resolution: Nullable[Resolution], selector: Func[IBaseData, T])RegisterIndicator[T](self: QCAlgorithm, symbol: Symbol, indicator: IndicatorBase[T], resolution: Nullable[TimeSpan], selector: Func[IBaseData, T])RegisterIndicator[T](self: QCAlgorithm, symbol: Symbol, indicator: IndicatorBase[T], consolidator: IDataConsolidator, selector: Func[IBaseData, T])RegisterIndicator(self: QCAlgorithm, symbol: Symbol, indicator: PyObject, resolution: Nullable[Resolution], selector: PyObject)RegisterIndicator(self: QCAlgorithm, symbol: Symbol, indicator: PyObject, resolution: Nullable[TimeSpan], selector: PyObject)RegisterIndicator(self: QCAlgorithm, symbol: Symbol, indicator: PyObject, consolidator: IDataConsolidator, selector: PyObject)

            Registers the consolidator to receive automatic 

             updates as well as configures the indicator to 

             receive updates

                    from the 

             consolidator.

        

        

            symbol: The symbol to register against

            indicator: The indicator to receive data from the 

             consolidator

        

            consolidator: The consolidator to receive raw subscription data

            selector: Selects a value from the BaseData send into the 

             indicator, if null defaults to a cast (x => (T)x)
        """
        pass

    def RemoveSecurity(self, symbol):
        """
        RemoveSecurity(self: QCAlgorithm, symbol: Symbol) -> bool

        

            Removes the security with the specified symbol. 

             This will cancel all

                    open orders and 

             then liquidate any existing holdings

        

        

            symbol: The symbol of the security to be removed
        """
        pass

    def ResolveConsolidator(self, symbol, *__args):
        """
        ResolveConsolidator(self: QCAlgorithm, symbol: Symbol, resolution: Nullable[Resolution], dataType: Type) -> IDataConsolidator

        ResolveConsolidator(self: QCAlgorithm, symbol: Symbol, timeSpan: Nullable[TimeSpan], dataType: Type) -> IDataConsolidator
        """
        pass

    def ROC(self, symbol, period, resolution, selector):
        """ ROC(self: QCAlgorithm, symbol: Symbol, period: int, resolution: Nullable[Resolution], selector: Func[IBaseData, Decimal]) -> RateOfChange """
        pass

    def ROCP(self, symbol, period, resolution, selector):
        """ ROCP(self: QCAlgorithm, symbol: Symbol, period: int, resolution: Nullable[Resolution], selector: Func[IBaseData, Decimal]) -> RateOfChangePercent """
        pass

    def ROCR(self, symbol, period, resolution, selector):
        """ ROCR(self: QCAlgorithm, symbol: Symbol, period: int, resolution: Nullable[Resolution], selector: Func[IBaseData, Decimal]) -> RateOfChangeRatio """
        pass

    def RSI(self, symbol, period, movingAverageType, resolution, selector):
        """ RSI(self: QCAlgorithm, symbol: Symbol, period: int, movingAverageType: MovingAverageType, resolution: Nullable[Resolution], selector: Func[IBaseData, Decimal]) -> RelativeStrengthIndex """
        pass

    def Sell(self, *__args):
        """
        Sell(self: QCAlgorithm, symbol: Symbol, quantity: int) -> OrderTicket

        

            Sell stock (alias of Order)

        

            symbol: string Symbol of the asset to trade

            quantity: int Quantity of the asset to trade

        Sell(self: QCAlgorithm, symbol: Symbol, quantity: float) -> OrderTicket

        

            Sell stock (alias of Order)

        

            symbol: String symbol to sell

            quantity: Quantity to order

            Returns: int Order Id.

        Sell(self: QCAlgorithm, symbol: Symbol, quantity: Single) -> OrderTicket

        

            Sell stock (alias of Order)

        

            symbol: String symbol

            quantity: Quantity to sell

            Returns: int order id

        Sell(self: QCAlgorithm, symbol: Symbol, quantity: Decimal) -> OrderTicket

        

            Sell stock (alias of Order)

        

            symbol: String symbol to sell

            quantity: Quantity to sell

            Returns: Int Order Id.

        Sell(self: QCAlgorithm, strategy: OptionStrategy, quantity: int) -> IEnumerable[OrderTicket]

        

            Sell Option Strategy (alias of Order)

        

            strategy: Specification of the strategy to trade

            quantity: Quantity of the strategy to trade

            Returns: Sequence of order ids
        """
        pass

    def SetAccountCurrency(self, accountCurrency):
        """
        SetAccountCurrency(self: QCAlgorithm, accountCurrency: str)

            Sets the account currency cash symbol this 

             algorithm is to manage.

        

        

            accountCurrency: The account currency cash symbol to set
        """
        pass

    def SetAlgorithmId(self, algorithmId):
        """
        SetAlgorithmId(self: QCAlgorithm, algorithmId: str)

            Set the algorithm id (backtestId or live deployId 

             for the algorithmm).

        

        

            algorithmId: String Algorithm Id
        """
        pass

    def SetAlpha(self, alpha):
        """
        SetAlpha(self: QCAlgorithm, alpha: PyObject)

            Sets the alpha model

        

            alpha: Model that generates alpha

        SetAlpha(self: QCAlgorithm, alpha: IAlphaModel)

            Sets the alpha model

        

            alpha: Model that generates alpha
        """
        pass

    def SetApi(self, api):
        """
        SetApi(self: QCAlgorithm, api: IApi)

            Provide the API for the algorithm.

        

            api: Initiated API
        """
        pass

    def SetAvailableDataTypes(self, availableDataTypes):
        """ SetAvailableDataTypes(self: QCAlgorithm, availableDataTypes: Dictionary[SecurityType, List[TickType]]) """
        pass

    def SetBenchmark(self, *__args):
        """
        SetBenchmark(self: QCAlgorithm, benchmark: PyObject)

            Sets the specified function as the benchmark, 

             this function provides the value of

                    

             the benchmark at each date/time requested

        

        

            benchmark: The benchmark producing function

        SetBenchmark(self: QCAlgorithm, securityType: SecurityType, symbol: str)

            Sets the benchmark used for computing statistics 

             of the algorithm to the specified symbol

        

        

            securityType: Is the symbol an equity, forex, base, etc. 

             Default SecurityType.Equity

        

            symbol: symbol to use as the benchmark

        SetBenchmark(self: QCAlgorithm, ticker: str)

            Sets the benchmark used for computing statistics 

             of the algorithm to the specified ticker, 

             defaulting to SecurityType.Equity

                    if 

             the ticker doesn't exist in the algorithm

        

        

            ticker: Ticker to use as the benchmark

        SetBenchmark(self: QCAlgorithm, symbol: Symbol)

            Sets the benchmark used for computing statistics 

             of the algorithm to the specified symbol

        

        

            symbol: symbol to use as the benchmark

        SetBenchmark(self: QCAlgorithm, benchmark: Func[DateTime, Decimal])
        """
        pass

    def SetBrokerageMessageHandler(self, handler):
        """
        SetBrokerageMessageHandler(self: QCAlgorithm, handler: IBrokerageMessageHandler)

            Sets the implementation used to handle messages 

             from the brokerage.

                    The default 

             implementation will forward messages to debug or 

             error

                    and when a 

             QuantConnect.Brokerages.BrokerageMessageType.Error

              occurs, the algorithm

                    is stopped.

        

        

            handler: The message handler to use
        """
        pass

    def SetBrokerageModel(self, *__args):
        """
        SetBrokerageModel(self: QCAlgorithm, model: PyObject)

            Sets the brokerage to emulate in backtesting or 

             paper trading.

                    This can be used to 

             set a custom brokerage model.

        

        

            model: The brokerage model to use

        SetBrokerageModel(self: QCAlgorithm, brokerage: BrokerageName, accountType: AccountType)

            Sets the brokerage to emulate in backtesting or 

             paper trading.

                    This can be used for 

             brokerages that have been implemented in LEAN

        

        

            brokerage: The brokerage to emulate

            accountType: The account type (Cash or Margin)

        SetBrokerageModel(self: QCAlgorithm, model: IBrokerageModel)

            Sets the brokerage to emulate in backtesting or 

             paper trading.

                    This can be used to 

             set a custom brokerage model.

        

        

            model: The brokerage model to use
        """
        pass

    def SetCash(self, *__args):
        """
        SetCash(self: QCAlgorithm, startingCash: float)

            Set initial cash for the strategy while 

             backtesting. During live mode this value is 

             ignored

                    and replaced with the actual 

             cash of your brokerage account.

        

        

            startingCash: Starting cash for the strategy backtest

        SetCash(self: QCAlgorithm, startingCash: int)

            Set initial cash for the strategy while 

             backtesting. During live mode this value is 

             ignored

                    and replaced with the actual 

             cash of your brokerage account.

        

        

            startingCash: Starting cash for the strategy backtest

        SetCash(self: QCAlgorithm, startingCash: Decimal)

            Set initial cash for the strategy while 

             backtesting. During live mode this value is 

             ignored

                    and replaced with the actual 

             cash of your brokerage account.

        

        

            startingCash: Starting cash for the strategy backtest

        SetCash(self: QCAlgorithm, symbol: str, startingCash: Decimal, conversionRate: Decimal)

            Set the cash for the specified symbol

        

            symbol: The cash symbol to set

            startingCash: Decimal cash value of portfolio

            conversionRate: The current conversion rate for the
        """
        pass

    def SetCurrentSlice(self, slice):
        """
        SetCurrentSlice(self: QCAlgorithm, slice: Slice)

            Sets the current slice

        

            slice: The Slice object
        """
        pass

    def SetDateTime(self, frontier):
        """
        SetDateTime(self: QCAlgorithm, frontier: DateTime)

            Update the internal algorithm time frontier.

        

            frontier: Current datetime.
        """
        pass

    def SetEndDate(self, *__args):
        """
        SetEndDate(self: QCAlgorithm, year: int, month: int, day: int)

            Set the end date for a backtest run

        

            year: Int year end date

            month: Int month end date

            day: Int end date 1-30

        SetEndDate(self: QCAlgorithm, end: DateTime)

            Set the end date for a backtest.

        

            end: Datetime value for end date
        """
        pass

    def SetExecution(self, execution):
        """
        SetExecution(self: QCAlgorithm, execution: PyObject)

            Sets the execution model

        

            execution: Model defining how to execute trades to reach a 

             portfolio target

        

        SetExecution(self: QCAlgorithm, execution: IExecutionModel)

            Sets the execution model

        

            execution: Model defining how to execute trades to reach a 

             portfolio target
        """
        pass

    def SetFinishedWarmingUp(self):
        """
        SetFinishedWarmingUp(self: QCAlgorithm)

            Sets 

             QuantConnect.Interfaces.IAlgorithm.IsWarmingUp to 

             false to indicate this algorithm has finished its 

             warm up
        """
        pass

    def SetFutureChainProvider(self, futureChainProvider):
        """
        SetFutureChainProvider(self: QCAlgorithm, futureChainProvider: IFutureChainProvider)

            Sets the future chain provider, used to get the 

             list of future contracts for an underlying symbol

        

        

            futureChainProvider: The future chain provider
        """
        pass

    def SetHistoryProvider(self, historyProvider):
        """
        SetHistoryProvider(self: QCAlgorithm, historyProvider: IHistoryProvider)

            Set the historical data provider

        

            historyProvider: Historical data provider
        """
        pass

    def SetHoldings(self, *__args):
        """
        SetHoldings(self: QCAlgorithm, targets: List[PortfolioTarget], liquidateExistingHoldings: bool)SetHoldings(self: QCAlgorithm, symbol: Symbol, percentage: float, liquidateExistingHoldings: bool)

            Alias for SetHoldings to avoid the M-decimal 

             errors.

        

        

            symbol: string symbol we wish to hold

            percentage: double percentage of holdings desired

            liquidateExistingHoldings: liquidate existing holdings if necessary to hold 

             this stock

        

        SetHoldings(self: QCAlgorithm, symbol: Symbol, percentage: Single, liquidateExistingHoldings: bool, tag: str)

            Alias for SetHoldings to avoid the M-decimal 

             errors.

        

        

            symbol: string symbol we wish to hold

            percentage: float percentage of holdings desired

            liquidateExistingHoldings: bool liquidate existing holdings if necessary to 

             hold this stock

        

            tag: Tag the order with a short string.

        SetHoldings(self: QCAlgorithm, symbol: Symbol, percentage: int, liquidateExistingHoldings: bool, tag: str)

            Alias for SetHoldings to avoid the M-decimal 

             errors.

        

        

            symbol: string symbol we wish to hold

            percentage: float percentage of holdings desired

            liquidateExistingHoldings: bool liquidate existing holdings if necessary to 

             hold this stock

        

            tag: Tag the order with a short string.

        SetHoldings(self: QCAlgorithm, symbol: Symbol, percentage: Decimal, liquidateExistingHoldings: bool, tag: str)

            Automatically place a market order which will set 

             the holdings to between 100% or -100% of 

             *PORTFOLIO VALUE*.

                    E.g. 

             SetHoldings("AAPL", 0.1); SetHoldings("IBM", 

             -0.2); -> Sets portfolio as long 10% APPL and 

             short 20% IBM

                    E.g. 

             SetHoldings("AAPL", 2); -> Sets apple to 2x 

             leveraged with all our cash.

                    If the 

             market is closed, place a market on open order.

        

        

            symbol: Symbol indexer

            percentage: decimal fraction of portfolio to set stock

            liquidateExistingHoldings: bool flag to clean all existing holdings before 

             setting new faction.

        

            tag: Tag the order with a short string.
        """
        pass

    def SetLiveMode(self, live):
        """
        SetLiveMode(self: QCAlgorithm, live: bool)

            Set live mode state of the algorithm run: Public 

             setter for the algorithm property LiveMode.
        """
        pass

    def SetLocked(self):
        """
        SetLocked(self: QCAlgorithm)

            Lock the algorithm initialization to avoid user 

             modifiying cash and data stream subscriptions
        """
        pass

    def SetMaximumOrders(self, max):
        """
        SetMaximumOrders(self: QCAlgorithm, max: int)

            Maximum number of orders for the algorithm
        """
        pass

    def SetObjectStore(self, objectStore):
        """
        SetObjectStore(self: QCAlgorithm, objectStore: IObjectStore)

            Sets the object store

        

            objectStore: The object store
        """
        pass

    def SetOptionChainProvider(self, optionChainProvider):
        """
        SetOptionChainProvider(self: QCAlgorithm, optionChainProvider: IOptionChainProvider)

            Sets the option chain provider, used to get the 

             list of option contracts for an underlying symbol

        

        

            optionChainProvider: The option chain provider
        """
        pass

    def SetPandasConverter(self):
        """
        SetPandasConverter(self: QCAlgorithm)

            Sets pandas converter
        """
        pass

    def SetParameters(self, parameters):
        """ SetParameters(self: QCAlgorithm, parameters: Dictionary[str, str]) """
        pass

    def SetPortfolioConstruction(self, portfolioConstruction):
        """
        SetPortfolioConstruction(self: QCAlgorithm, portfolioConstruction: PyObject)

            Sets the portfolio construction model

        

            portfolioConstruction: Model defining how to build a portfolio from 

             alphas

        

        SetPortfolioConstruction(self: QCAlgorithm, portfolioConstruction: IPortfolioConstructionModel)

            Sets the portfolio construction model

        

            portfolioConstruction: Model defining how to build a portfolio from 

             insights
        """
        pass

    def SetQuit(self, quit):
        """
        SetQuit(self: QCAlgorithm, quit: bool)

            Set the Quit flag property of the algorithm.

        

            quit: Boolean quit state
        """
        pass

    def SetRiskManagement(self, riskManagement):
        """
        SetRiskManagement(self: QCAlgorithm, riskManagement: PyObject)

            Sets the risk management model

        

            riskManagement: Model defining how risk is managed

        SetRiskManagement(self: QCAlgorithm, riskManagement: IRiskManagementModel)

            Sets the risk management model

        

            riskManagement: Model defining how risk is managed
        """
        pass

    def SetRunTimeError(self, exception):
        """
        SetRunTimeError(self: QCAlgorithm, exception: Exception)

            Set the runtime error

        

            exception: Represents error that occur during execution
        """
        pass

    def SetRuntimeStatistic(self, name, value):
        """
        SetRuntimeStatistic(self: QCAlgorithm, name: str, value: str)

            Set a runtime statistic for the algorithm. 

             Runtime statistics are shown in the top banner of 

             a live algorithm GUI.

        

        

            name: Name of your runtime statistic

            value: String value of your runtime statistic

        SetRuntimeStatistic(self: QCAlgorithm, name: str, value: Decimal)

            Set a runtime statistic for the algorithm. 

             Runtime statistics are shown in the top banner of 

             a live algorithm GUI.

        

        

            name: Name of your runtime statistic

            value: Decimal value of your runtime statistic

        SetRuntimeStatistic(self: QCAlgorithm, name: str, value: int)

            Set a runtime statistic for the algorithm. 

             Runtime statistics are shown in the top banner of 

             a live algorithm GUI.

        

        

            name: Name of your runtime statistic

            value: Int value of your runtime statistic

        SetRuntimeStatistic(self: QCAlgorithm, name: str, value: float)

            Set a runtime statistic for the algorithm. 

             Runtime statistics are shown in the top banner of 

             a live algorithm GUI.

        

        

            name: Name of your runtime statistic

            value: Double value of your runtime statistic
        """
        pass

    def SetSecurityInitializer(self, securityInitializer):
        """
        SetSecurityInitializer(self: QCAlgorithm, securityInitializer: PyObject)

            Sets the security initializer function, used to 

             initialize/configure securities after creation

        

        

            securityInitializer: The security initializer function or class

        SetSecurityInitializer(self: QCAlgorithm, securityInitializer: ISecurityInitializer)

            Sets the security initializer, used to 

             initialize/configure securities after creation.

         

                        The initializer will be applied to all 

             universes and manually added securities.

        

        

            securityInitializer: The security initializer

        SetSecurityInitializer(self: QCAlgorithm, securityInitializer: Action[Security, bool])SetSecurityInitializer(self: QCAlgorithm, securityInitializer: Action[Security])
        """
        pass

    def SetStartDate(self, *__args):
        """
        SetStartDate(self: QCAlgorithm, year: int, month: int, day: int)

            Set the start date for backtest.

        

            year: Int year starting date

            month: Int month starting date

            day: Int starting date 1-30

        SetStartDate(self: QCAlgorithm, start: DateTime)

            Set the start date for the backtest

        

            start: Datetime Start date for backtest
        """
        pass

    def SetStatus(self, status):
        """
        SetStatus(self: QCAlgorithm, status: AlgorithmStatus)

            Set the state of a live deployment

        

            status: Live deployment status
        """
        pass

    def SetTimeZone(self, timeZone):
        """
        SetTimeZone(self: QCAlgorithm, timeZone: str)

            Sets the time zone of the 

             QuantConnect.Algorithm.QCAlgorithm.Time property 

             in the algorithm

        

        

            timeZone: The desired time zone

        SetTimeZone(self: QCAlgorithm, timeZone: DateTimeZone)

            Sets the time zone of the 

             QuantConnect.Algorithm.QCAlgorithm.Time property 

             in the algorithm

        

        

            timeZone: The desired time zone
        """
        pass

    def SetTradeBuilder(self, tradeBuilder):
        """
        SetTradeBuilder(self: QCAlgorithm, tradeBuilder: ITradeBuilder)

            Set the QuantConnect.Interfaces.ITradeBuilder 

             implementation to generate trades from executions 

             and market price updates
        """
        pass

    def SetUniverseSelection(self, universeSelection):
        """
        SetUniverseSelection(self: QCAlgorithm, universeSelection: PyObject)

            Sets the universe selection model

        

            universeSelection: Model defining universes for the algorithm

        SetUniverseSelection(self: QCAlgorithm, universeSelection: IUniverseSelectionModel)

            Sets the universe selection model

        

            universeSelection: Model defining universes for the algorithm
        """
        pass

    def SetWarmUp(self, *__args):
        """
        SetWarmUp(self: QCAlgorithm, timeSpan: TimeSpan)

            Sets the warm up period to the specified value

        

            timeSpan: The amount of time to warm up, this does not take 

             into account market hours/weekends

        

        SetWarmUp(self: QCAlgorithm, timeSpan: TimeSpan, resolution: Resolution)

            Sets the warm up period to the specified value

        

            timeSpan: The amount of time to warm up, this does not take 

             into account market hours/weekends

        

            resolution: The resolution to request

        SetWarmUp(self: QCAlgorithm, barCount: int)

            Sets the warm up period by resolving a start date 

             that would send that amount of data into

                

                 the algorithm. The highest (smallest) 

             resolution in the securities collection will be 

             used.

                    For example, if an algorithm 

             has minute and daily data and 200 bars are 

             requested, that would

                    use 200 minute 

             bars.

        

        

            barCount: The number of data points requested for warm up

        SetWarmUp(self: QCAlgorithm, barCount: int, resolution: Resolution)

            Sets the warm up period by resolving a start date 

             that would send that amount of data into

                

                 the algorithm.

        

        

            barCount: The number of data points requested for warm up

            resolution: The resolution to request
        """
        pass

    def SetWarmup(self, *__args):
        """
        SetWarmup(self: QCAlgorithm, timeSpan: TimeSpan)

            Sets the warm up period to the specified value

        

            timeSpan: The amount of time to warm up, this does not take 

             into account market hours/weekends

        

        SetWarmup(self: QCAlgorithm, timeSpan: TimeSpan, resolution: Resolution)

            Sets the warm up period to the specified value

        

            timeSpan: The amount of time to warm up, this does not take 

             into account market hours/weekends

        

            resolution: The resolution to request

        SetWarmup(self: QCAlgorithm, barCount: int)

            Sets the warm up period by resolving a start date 

             that would send that amount of data into

                

                 the algorithm. The highest (smallest) 

             resolution in the securities collection will be 

             used.

                    For example, if an algorithm 

             has minute and daily data and 200 bars are 

             requested, that would

                    use 200 minute 

             bars.

        

        

            barCount: The number of data points requested for warm up

        SetWarmup(self: QCAlgorithm, barCount: int, resolution: Resolution)

            Sets the warm up period by resolving a start date 

             that would send that amount of data into

                

                 the algorithm.

        

        

            barCount: The number of data points requested for warm up

            resolution: The resolution to request
        """
        pass

    def SMA(self, symbol, period, resolution, selector):
        """ SMA(self: QCAlgorithm, symbol: Symbol, period: int, resolution: Nullable[Resolution], selector: Func[IBaseData, Decimal]) -> SimpleMovingAverage """
        pass

    def STD(self, symbol, period, resolution, selector):
        """ STD(self: QCAlgorithm, symbol: Symbol, period: int, resolution: Nullable[Resolution], selector: Func[IBaseData, Decimal]) -> StandardDeviation """
        pass

    def STO(self, symbol, period, *__args):
        """
        STO(self: QCAlgorithm, symbol: Symbol, period: int, kPeriod: int, dPeriod: int, resolution: Nullable[Resolution]) -> Stochastic

        STO(self: QCAlgorithm, symbol: Symbol, period: int, resolution: Nullable[Resolution]) -> Stochastic
        """
        pass

    def StopLimitOrder(self, symbol, quantity, stopPrice, limitPrice, tag):
        """
        StopLimitOrder(self: QCAlgorithm, symbol: Symbol, quantity: int, stopPrice: Decimal, limitPrice: Decimal, tag: str) -> OrderTicket

        

            Send a stop limit order to the transaction 

             handler:

        

        

            symbol: String symbol for the asset

            quantity: Quantity of shares for limit order

            stopPrice: Stop price for this order

            limitPrice: Limit price to fill this order

            tag: String tag for the order (optional)

            Returns: Order id

        StopLimitOrder(self: QCAlgorithm, symbol: Symbol, quantity: float, stopPrice: Decimal, limitPrice: Decimal, tag: str) -> OrderTicket

        

            Send a stop limit order to the transaction 

             handler:

        

        

            symbol: String symbol for the asset

            quantity: Quantity of shares for limit order

            stopPrice: Stop price for this order

            limitPrice: Limit price to fill this order

            tag: String tag for the order (optional)

            Returns: Order id

        StopLimitOrder(self: QCAlgorithm, symbol: Symbol, quantity: Decimal, stopPrice: Decimal, limitPrice: Decimal, tag: str) -> OrderTicket

        

            Send a stop limit order to the transaction 

             handler:

        

        

            symbol: String symbol for the asset

            quantity: Quantity of shares for limit order

            stopPrice: Stop price for this order

            limitPrice: Limit price to fill this order

            tag: String tag for the order (optional)

            Returns: Order id
        """
        pass

    def StopMarketOrder(self, symbol, quantity, stopPrice, tag):
        """
        StopMarketOrder(self: QCAlgorithm, symbol: Symbol, quantity: int, stopPrice: Decimal, tag: str) -> OrderTicket

        

            Create a stop market order and return the newly 

             created order id; or negative if the order is 

             invalid

        

        

            symbol: String symbol for the asset we're trading

            quantity: Quantity to be traded

            stopPrice: Price to fill the stop order

            tag: Optional string data tag for the order

            Returns: Int orderId for the new order.

        StopMarketOrder(self: QCAlgorithm, symbol: Symbol, quantity: float, stopPrice: Decimal, tag: str) -> OrderTicket

        

            Create a stop market order and return the newly 

             created order id; or negative if the order is 

             invalid

        

        

            symbol: String symbol for the asset we're trading

            quantity: Quantity to be traded

            stopPrice: Price to fill the stop order

            tag: Optional string data tag for the order

            Returns: Int orderId for the new order.

        StopMarketOrder(self: QCAlgorithm, symbol: Symbol, quantity: Decimal, stopPrice: Decimal, tag: str) -> OrderTicket

        

            Create a stop market order and return the newly 

             created order id; or negative if the order is 

             invalid

        

        

            symbol: String symbol for the asset we're trading

            quantity: Quantity to be traded

            stopPrice: Price to fill the stop order

            tag: Optional string data tag for the order

            Returns: Int orderId for the new order.
        """
        pass

    def SUM(self, symbol, period, resolution, selector):
        """ SUM(self: QCAlgorithm, symbol: Symbol, period: int, resolution: Nullable[Resolution], selector: Func[IBaseData, Decimal]) -> Sum """
        pass

    def SWISS(self, symbol, period, delta, tool, resolution, selector):
        """ SWISS(self: QCAlgorithm, symbol: Symbol, period: int, delta: float, tool: SwissArmyKnifeTool, resolution: Nullable[Resolution], selector: Func[IBaseData, Decimal]) -> SwissArmyKnife """
        pass

    def Symbol(self, ticker):
        """
        Symbol(self: QCAlgorithm, ticker: str) -> Symbol

        

            Converts the string 'ticker' symbol into a full 

             QuantConnect.Algorithm.QCAlgorithm.Symbol(System.S

             tring) object

                    This requires that the 

             string 'ticker' has been added to the algorithm

        

        

            ticker: The ticker symbol. This should be the ticker 

             symbol

                    as it was added to the 

             algorithm

        

            Returns: The symbol object mapped to the specified ticker
        """
        pass

    def T3(self, symbol, period, volumeFactor, resolution, selector):
        """ T3(self: QCAlgorithm, symbol: Symbol, period: int, volumeFactor: Decimal, resolution: Nullable[Resolution], selector: Func[IBaseData, Decimal]) -> T3MovingAverage """
        pass

    def TEMA(self, symbol, period, resolution, selector):
        """ TEMA(self: QCAlgorithm, symbol: Symbol, period: int, resolution: Nullable[Resolution], selector: Func[IBaseData, Decimal]) -> TripleExponentialMovingAverage """
        pass

    def TR(self, symbol, resolution, selector):
        """ TR(self: QCAlgorithm, symbol: Symbol, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> TrueRange """
        pass

    def Train(self, *__args):
        """
        Train(self: QCAlgorithm, trainingCode: PyObject) -> ScheduledEvent

        

            Schedules the provided training code to execute 

             immediately

        

        

            trainingCode: The training code to be invoked

        Train(self: QCAlgorithm, dateRule: IDateRule, timeRule: ITimeRule, trainingCode: PyObject) -> ScheduledEvent

        

            Schedules the training code to run using the 

             specified date and time rules

        

        

            dateRule: Specifies what dates the event should run

            timeRule: Specifies the times on those dates the event 

             should run

        

            trainingCode: The training code to be invoked

        Train(self: QCAlgorithm, dateRule: IDateRule, timeRule: ITimeRule, trainingCode: Action) -> ScheduledEvent

        

            Schedules the training code to run using the 

             specified date and time rules

        

        

            dateRule: Specifies what dates the event should run

            timeRule: Specifies the times on those dates the event 

             should run

        

            trainingCode: The training code to be invoked

        Train(self: QCAlgorithm, trainingCode: Action) -> ScheduledEvent

        

            Schedules the provided training code to execute 

             immediately

        

        

            trainingCode: The training code to be invoked
        """
        pass

    def TRIMA(self, symbol, period, resolution, selector):
        """ TRIMA(self: QCAlgorithm, symbol: Symbol, period: int, resolution: Nullable[Resolution], selector: Func[IBaseData, Decimal]) -> TriangularMovingAverage """
        pass

    def TRIX(self, symbol, period, resolution, selector):
        """ TRIX(self: QCAlgorithm, symbol: Symbol, period: int, resolution: Nullable[Resolution], selector: Func[IBaseData, Decimal]) -> Trix """
        pass

    def ULTOSC(self, symbol, period1, period2, period3, resolution, selector):
        """ ULTOSC(self: QCAlgorithm, symbol: Symbol, period1: int, period2: int, period3: int, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> UltimateOscillator """
        pass

    def VAR(self, symbol, period, resolution, selector):
        """ VAR(self: QCAlgorithm, symbol: Symbol, period: int, resolution: Nullable[Resolution], selector: Func[IBaseData, Decimal]) -> Variance """
        pass

    def VWAP(self, symbol, period=None, resolution=None, selector=None):
        """
        VWAP(self: QCAlgorithm, symbol: Symbol, period: int, resolution: Nullable[Resolution], selector: Func[IBaseData, TradeBar]) -> VolumeWeightedAveragePriceIndicator

        VWAP(self: QCAlgorithm, symbol: Symbol) -> IntradayVwap

        

            Creates the canonical VWAP indicator that resets 

             each day. The indicator will be automatically

           

                      updated on the security's configured 

             resolution.

        

        

            symbol: The symbol whose VWAP we want

            Returns: The IntradayVWAP for the specified symbol
        """
        pass

    def WarmUpIndicator(self, symbol, indicator, *__args):
        """
        WarmUpIndicator(self: QCAlgorithm, symbol: Symbol, indicator: IndicatorBase[IndicatorDataPoint], resolution: Nullable[Resolution], selector: Func[IBaseData, Decimal]) -> IndicatorBase[IndicatorDataPoint]

        WarmUpIndicator(self: QCAlgorithm, symbol: Symbol, indicator: IndicatorBase[IndicatorDataPoint], period: TimeSpan, selector: Func[IBaseData, Decimal]) -> IndicatorBase[IndicatorDataPoint]

        WarmUpIndicator[T](self: QCAlgorithm, symbol: Symbol, indicator: IndicatorBase[T], resolution: Nullable[Resolution], selector: Func[IBaseData, T]) -> IndicatorBase[T]

        WarmUpIndicator[T](self: QCAlgorithm, symbol: Symbol, indicator: IndicatorBase[T], period: TimeSpan, selector: Func[IBaseData, T]) -> IndicatorBase[T]
        """
        pass

    def WILR(self, symbol, period, resolution, selector):
        """ WILR(self: QCAlgorithm, symbol: Symbol, period: int, resolution: Nullable[Resolution], selector: Func[IBaseData, IBaseDataBar]) -> WilliamsPercentR """
        pass

    def WWMA(self, symbol, period, resolution, selector):
        """ WWMA(self: QCAlgorithm, symbol: Symbol, period: int, resolution: Nullable[Resolution], selector: Func[IBaseData, Decimal]) -> WilderMovingAverage """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AccountCurrency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the account currency



Get: AccountCurrency(self: QCAlgorithm) -> str



"""

    ActiveSecurities = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Read-only dictionary containing all active securities. An active security is

            a security that is currently selected by the universe or has holdings or open orders.



Get: ActiveSecurities(self: QCAlgorithm) -> IReadOnlyDictionary[Symbol, Security]



"""

    AlgorithmId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Algorithm Id for this backtest or live algorithm.



Get: AlgorithmId(self: QCAlgorithm) -> str



"""

    Alpha = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the alpha model



Get: Alpha(self: QCAlgorithm) -> IAlphaModel



Set: Alpha(self: QCAlgorithm) = value

"""

    Benchmark = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Benchmark



Get: Benchmark(self: QCAlgorithm) -> IBenchmark



"""

    BrokerageMessageHandler = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the brokerage message handler used to decide what to do

            with each message sent from the brokerage



Get: BrokerageMessageHandler(self: QCAlgorithm) -> IBrokerageMessageHandler



Set: BrokerageMessageHandler(self: QCAlgorithm) = value

"""

    BrokerageModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the brokerage model - used to model interactions with specific brokerages.



Get: BrokerageModel(self: QCAlgorithm) -> IBrokerageModel



"""

    CandlestickPatterns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an instance to access the candlestick pattern helper methods



Get: CandlestickPatterns(self: QCAlgorithm) -> CandlestickPatterns



"""

    CurrentSlice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the current Slice object



Get: CurrentSlice(self: QCAlgorithm) -> Slice



"""

    DateRules = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the date rules helper object to make specifying dates for events easier



Get: DateRules(self: QCAlgorithm) -> DateRules



"""

    DebugMessages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Storage for debugging messages before the event handler has passed control back to the Lean Engine.



Get: DebugMessages(self: QCAlgorithm) -> ConcurrentQueue[str]



Set: DebugMessages(self: QCAlgorithm) = value

"""

    DebugMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Enables additional logging of framework models including:

            All insights, portfolio targets, order events, and any risk management altered targets



Get: DebugMode(self: QCAlgorithm) -> bool



Set: DebugMode(self: QCAlgorithm) = value

"""

    DefaultOrderProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the default order properties



Get: DefaultOrderProperties(self: QCAlgorithm) -> IOrderProperties



Set: DefaultOrderProperties(self: QCAlgorithm) = value

"""

    EnableAutomaticIndicatorWarmUp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets whether or not WarmUpIndicator is allowed to warm up indicators/>



Get: EnableAutomaticIndicatorWarmUp(self: QCAlgorithm) -> bool



Set: EnableAutomaticIndicatorWarmUp(self: QCAlgorithm) = value

"""

    EndDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Value of the user set start-date from the backtest. Controls the period of the backtest.



Get: EndDate(self: QCAlgorithm) -> DateTime



"""

    ErrorMessages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """List of error messages generated by the user's code calling the "Error" function.



Get: ErrorMessages(self: QCAlgorithm) -> ConcurrentQueue[str]



Set: ErrorMessages(self: QCAlgorithm) = value

"""

    Execution = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the execution model



Get: Execution(self: QCAlgorithm) -> IExecutionModel



Set: Execution(self: QCAlgorithm) = value

"""

    FutureChainProvider = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the future chain provider, used to get the list of future contracts for an underlying symbol



Get: FutureChainProvider(self: QCAlgorithm) -> IFutureChainProvider



"""

    HistoryProvider = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the history provider for the algorithm



Get: HistoryProvider(self: QCAlgorithm) -> IHistoryProvider



Set: HistoryProvider(self: QCAlgorithm) = value

"""

    IsWarmingUp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets whether or not this algorithm is still warming up



Get: IsWarmingUp(self: QCAlgorithm) -> bool



"""

    LiveMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Boolean property indicating the algorithm is currently running in live mode.



Get: LiveMode(self: QCAlgorithm) -> bool



"""

    LogMessages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Storage for log messages before the event handlers have passed control back to the Lean Engine.



Get: LogMessages(self: QCAlgorithm) -> ConcurrentQueue[str]



Set: LogMessages(self: QCAlgorithm) = value

"""

    MarketHoursDatabase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the market hours database in use by this algorithm



"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Public name for the algorithm as automatically generated by the IDE. Intended for helping distinguish logs by noting

            the algorithm-id.



Get: Name(self: QCAlgorithm) -> str



Set: Name(self: QCAlgorithm) = value

"""

    Notify = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Notification Manager for Sending Live Runtime Notifications to users about important events.



Get: Notify(self: QCAlgorithm) -> NotificationManager



Set: Notify(self: QCAlgorithm) = value

"""

    ObjectStore = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the object store, used for persistence



Get: ObjectStore(self: QCAlgorithm) -> ObjectStore



"""

    OptionChainProvider = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the option chain provider, used to get the list of option contracts for an underlying symbol



Get: OptionChainProvider(self: QCAlgorithm) -> IOptionChainProvider



"""

    PandasConverter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PandasConverter(self: QCAlgorithm) -> PandasConverter



"""

    Portfolio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Portfolio object provieds easy access to the underlying security-holding properties; summed together in a way to make them useful.

            This saves the user time by providing common portfolio requests in a single



Get: Portfolio(self: QCAlgorithm) -> SecurityPortfolioManager



Set: Portfolio(self: QCAlgorithm) = value

"""

    PortfolioConstruction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the portfolio construction model



Get: PortfolioConstruction(self: QCAlgorithm) -> IPortfolioConstructionModel



Set: PortfolioConstruction(self: QCAlgorithm) = value

"""

    RiskManagement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the risk management model



Get: RiskManagement(self: QCAlgorithm) -> IRiskManagementModel



Set: RiskManagement(self: QCAlgorithm) = value

"""

    RunTimeError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the run time error from the algorithm, or null if none was encountered.



Get: RunTimeError(self: QCAlgorithm) -> Exception



Set: RunTimeError(self: QCAlgorithm) = value

"""

    RuntimeStatistics = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Access to the runtime statistics property. User provided statistics.



Get: RuntimeStatistics(self: QCAlgorithm) -> ConcurrentDictionary[str, str]



"""

    Schedule = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets schedule manager for adding/removing scheduled events



Get: Schedule(self: QCAlgorithm) -> ScheduleManager



"""

    Securities = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Security collection is an array of the security objects such as Equities and FOREX. Securities data

            manages the properties of tradeable assets such as price, open and close time and holdings information.



Get: Securities(self: QCAlgorithm) -> SecurityManager



Set: Securities(self: QCAlgorithm) = value

"""

    SecurityInitializer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an instance that is to be used to initialize newly created securities.



Get: SecurityInitializer(self: QCAlgorithm) -> ISecurityInitializer



"""

    Settings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the user settings for the algorithm



Get: Settings(self: QCAlgorithm) -> IAlgorithmSettings



"""

    StartDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Value of the user set start-date from the backtest.



Get: StartDate(self: QCAlgorithm) -> DateTime



"""

    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the current status of the algorithm



Get: Status(self: QCAlgorithm) -> AlgorithmStatus



Set: Status(self: QCAlgorithm) = value

"""

    SubscriptionManager = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Generic Data Manager - Required for compiling all data feeds in order, and passing them into algorithm event methods.

            The subscription manager contains a list of the data feed's we're subscribed to and properties of each data feed.



Get: SubscriptionManager(self: QCAlgorithm) -> SubscriptionManager



Set: SubscriptionManager(self: QCAlgorithm) = value

"""

    SymbolPropertiesDatabase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the symbol properties database in use by this algorithm



"""

    Time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Read-only value for current time frontier of the algorithm in terms of the QuantConnect.Algorithm.QCAlgorithm.TimeZone



Get: Time(self: QCAlgorithm) -> DateTime



"""

    TimeKeeper = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the time keeper instance



Get: TimeKeeper(self: QCAlgorithm) -> ITimeKeeper



"""

    TimeRules = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the time rules helper object to make specifying times for events easier



Get: TimeRules(self: QCAlgorithm) -> TimeRules



"""

    TimeZone = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the time zone used for the QuantConnect.Algorithm.QCAlgorithm.Time property. The default value

            is QuantConnect.TimeZones.NewYork



Get: TimeZone(self: QCAlgorithm) -> DateTimeZone



"""

    TradeBuilder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Trade Builder to generate trades from executions



Get: TradeBuilder(self: QCAlgorithm) -> ITradeBuilder



"""

    TradingCalendar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets trading calendar populated with trading events



Get: TradingCalendar(self: QCAlgorithm) -> TradingCalendar



"""

    Transactions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Transaction Manager - Process transaction fills and order management.



Get: Transactions(self: QCAlgorithm) -> SecurityTransactionManager



Set: Transactions(self: QCAlgorithm) = value

"""

    Universe = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a helper that provides pre-defined universe definitions, such as top dollar volume



Get: Universe(self: QCAlgorithm) -> UniverseDefinitions



"""

    UniverseManager = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets universe manager which holds universes keyed by their symbol



Get: UniverseManager(self: QCAlgorithm) -> UniverseManager



"""

    UniverseSelection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the universe selection model.



Get: UniverseSelection(self: QCAlgorithm) -> IUniverseSelectionModel



Set: UniverseSelection(self: QCAlgorithm) = value

"""

    UniverseSettings = UniverseSettings   # default
    """Gets the universe settings to be used when adding securities via universe selection



Get: UniverseSettings(self: QCAlgorithm) -> UniverseSettings



"""

    UtcTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Current date/time in UTC.



Get: UtcTime(self: QCAlgorithm) -> DateTime



"""


    InsightsGenerated = None


class UniverseDefinitions(object):
    """
    Provides helpers for defining universes in algorithms

    

    UniverseDefinitions(algorithm: QCAlgorithm)
    """
    @staticmethod # known case of __new__
    def __new__(self, algorithm):
        """ __new__(cls: type, algorithm: QCAlgorithm) """
        pass

    Constituent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a helper that provides methods for creating constituent universes



Get: Constituent(self: UniverseDefinitions) -> ConstituentUniverseDefinitions



"""

    DollarVolume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a helper that provides methods for creating universes based on daily dollar volumes



Get: DollarVolume(self: UniverseDefinitions) -> DollarVolumeUniverseDefinitions



"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a helper that provides methods for creating universes based on index definitions



Get: Index(self: UniverseDefinitions) -> IndexUniverseDefinitions



"""

    Unchanged = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies that universe selection should not make changes on this iteration



Get: Unchanged(self: UniverseDefinitions) -> UnchangedUniverse



"""



# variables with complex values

