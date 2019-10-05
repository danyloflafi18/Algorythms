package drawManager;

public final class DrawManager {

    public int sumElementsOfArray(Integer[] array, int lastIndex) {
        int result = 0;
        for (int i = 0; i < lastIndex; i++) {
            result += array[i];
        }
        return result;
    }


    public Integer[] bubbleSortOfArray(Integer[] array) {
        boolean swap = true;

        while (swap) {
            swap = false;

            for (int i = 0; i < array.length - 1; i++) {
                if (array[i] > array[i + 1]) {
                    int temp = array[i];
                    array[i] = array[i + 1];
                    array[i + 1] = temp;
                    swap = true;
                }
            }
        }

        return array;
    }

    public int measureExecutionTime(int paintersQuantity, int minutesForOneMeter, Integer[] billboardsLength) {

        int result = 0;
        Integer[] sortedArray = this.bubbleSortOfArray(billboardsLength);
        if (paintersQuantity >= billboardsLength.length) {
            result = minutesForOneMeter * sortedArray[sortedArray.length - 1];
        }else if (paintersQuantity < billboardsLength.length) {
            result = (sumElementsOfArray(sortedArray,billboardsLength.length - paintersQuantity
            ) + sortedArray[sortedArray.length - 1]) * minutesForOneMeter;

        }
        return result;
    }
}












